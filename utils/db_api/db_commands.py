from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        user_id BIGINT NOT NULL UNIQUE,
        has_acsess TEXT 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_admin(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Admin (
        id SERIAL PRIMARY KEY,
        word TEXT UNIQUE,
        members BigInt,
        power TEXT,
        chat_id BigInt
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_groups(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Groups (
        id SERIAL PRIMARY KEY,
        chat_id BigInt UNIQUE,
        link TEXT UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_bad_words(self):
        sql = """
        CREATE TABLE IF NOT EXISTS BadWords (
        id SERIAL PRIMARY KEY,
        badword TEXT UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_is_added(self):
        sql = """
        CREATE TABLE IF NOT EXISTS AddMember (
        id SERIAL PRIMARY KEY,
        user_id BigInt UNIQUE NOT NULL,
        is_added BigInt
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name: str, username: str, user_id: int, has_acsess: str):
        sql = "INSERT INTO users (full_name, username, user_id, has_acsess) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, full_name, username, user_id, has_acsess, fetchrow=True)

    async def add_members_to_adminpanel(self, members, chat_id, power):
        sql = "INSERT INTO Admin (members, chat_id, power) VALUES($1, $2, $3)"
        return await self.execute(sql, members, chat_id, power, fetchrow=True)

    async def add_id_to_addmember(self, user_id, is_added):
        sql = "INSERT INTO AddMember (user_id, is_added) VALUES($1, $2)"
        return await self.execute(sql, user_id, is_added, fetchrow=True)

    async def add_word_to_bad_word(self, badword):
        sql = "INSERT INTO BadWords (badword) VALUES($1)"
        return await self.execute(sql, badword, fetchrow=True)

    async def add_id_of_group(self, chat_id, link):
        sql = "INSERT INTO Groups (chat_id, link) VALUES($1, $2)"
        return await self.execute(sql, chat_id, link, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_many_member(self):
        sql = "SELECT members, chat_id, power FROM Admin"
        return await self.execute(sql, fetch=True)

    async def select_all_badwrods(self):
        sql = "SELECT badword FROM BadWords"
        return await self.execute(sql, fetch=True)

    # async def select_on_off(self, chat_id):
    #     sql = "SELECT on_off FROM Groups WHERE chat_id=$1"
    #     return await self.execute(sql, chat_id, fetch=True)

    async def select_all_group(self):
        sql = "SELECT * FROM Groups"
        return await self.execute(sql, fetch=True)

    async def select_one_users(self, user_id):
        sql = "SELECT * FROM Users WHERE user_id=$1"
        return await self.execute(sql, user_id, fetch=True)

    async def select_add_member(self, user_id):
        sql = "SELECT is_added FROM AddMember WHERE user_id=$1"
        return await self.execute(sql, user_id, fetch=True)


    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_bot_on_off(self, on_off, chat_id):
        sql = "UPDATE Groups SET on_off=$1 WHERE chat_id=$2"
        return await self.execute(sql, on_off, chat_id, execute=True)

    async def update_power(self, power, chat_id):
        sql = "UPDATE Admin SET power=$1 WHERE chat_id=$2"
        return await self.execute(sql, power, chat_id, execute=True)

    async def update_add_members(self, members, chat_id):
        sql = "UPDATE Admin SET members=$1 WHERE chat_id=$2"
        return await self.execute(sql, members, chat_id, execute=True)

    async def update_add_member(self, is_added, user_id):
        sql = "UPDATE AddMember SET is_added=$1 WHERE user_id=$2"
        return await self.execute(sql, is_added, user_id, execute=True)

    async def update_group_id(self, chat_id):
        sql = "UPDATE Groups SET chat_id=$1 WHERE chat_id=$1"
        return await self.execute(sql, chat_id, execute=True)

    # async def update_acsess_user(self, has_acsess, user_id):
    #     sql = "UPDATE Groups SET has_acsess=$1 WHERE link=$2"
    #     return await self.execute(sql, chat_id, link, execute=True)

    async def delete_user(self, user_id):
        sql = "DELETE FROM Users WHERE user_id=$1"
        await self.execute(sql, user_id, execute=True)

    async def delete_bad_word(self, badword):
        sql = "DELETE FROM BadWords WHERE badword=$1"
        await self.execute(sql, badword, execute=True)


    async def drop_courses(self):
        await self.execute("DROP TABLE Courses", execute=True)