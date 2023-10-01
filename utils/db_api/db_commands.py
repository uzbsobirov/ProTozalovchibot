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
        user_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_users_data(self):
        sql = """
        CREATE TABLE IF NOT EXISTS UsersData (
        id SERIAL PRIMARY KEY,
        user_id BIGINT NOT NULL,
        add_members BigInt,
        chat_id BigInt,
        chat_link TEXT
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_group_data(self):
        sql = """
        CREATE TABLE IF NOT EXISTS ListGroups (
        id SERIAL PRIMARY KEY,
        chat_id BigInt UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_group_required(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Required (
        id SERIAL PRIMARY KEY,
        chat_id BigInt UNIQUE,
        chat_link TEXT,
        method TEXT,
        amount BigInt NULL
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_group_badwords(self):
        sql = """
        CREATE TABLE IF NOT EXISTS BadWords (
        id SERIAL PRIMARY KEY,
        chat_id BigInt UNIQUE,
        words TEXT UNIQUE
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

    async def add_group(self, chat_id: str):
        sql = "INSERT INTO ListGroups (chat_id) VALUES($1) returning *"
        return await self.execute(sql, chat_id, fetchrow=True)

    async def add_user_data(self, user_id: int, add_members: int, chat_id: int, chat_link: str):
        sql = "INSERT INTO UsersData (user_id, add_members, chat_id, chat_link) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, user_id, add_members, chat_id, chat_link, fetchrow=True)

    async def add_group_required(self, chat_id: int, chat_link: str, method: str, amount: int):
        sql = "INSERT INTO Required (chat_id, chat_link, method, amount) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, chat_id, chat_link, method, amount, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_required_groups(self):
        sql = "SELECT * FROM Required"
        return await self.execute(sql, fetch=True)

    async def select_all_users_data(self):
        sql = "SELECT * FROM UsersData"
        return await self.execute(sql, fetch=True)

    async def select_one_user(self, user_id):
        sql = "SELECT * FROM UsersData WHERE user_id=$1"
        return await self.execute(sql, user_id, fetch=True)

    async def select_one_group(self, chat_id):
        sql = "SELECT * FROM Required WHERE chat_id=$1"
        return await self.execute(sql, chat_id, fetch=True)

    async def select_one_user_data(self, user_id, chat_id):
        sql = "SELECT * FROM UsersData WHERE user_id=$1 and chat_id=$2"
        return await self.execute(sql, user_id, chat_id, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_members(self, add_members, chat_id, user_id):
        sql = "UPDATE UsersData SET add_members=$1 WHERE chat_id=$2 and user_id=$3"
        return await self.execute(sql, add_members, chat_id, user_id, execute=True)

    async def update_required_members(self, amount, chat_id):
        sql = "UPDATE Required SET amount=$1 WHERE chat_id=$2"
        return await self.execute(sql, amount, chat_id, execute=True)

    async def delete_user(self, user_id):
        sql = "DELETE FROM Users WHERE user_id=$1"
        await self.execute(sql, user_id, execute=True)

    async def delete_required_group(self, chat_id):
        sql = "DELETE FROM Required WHERE chat_id=$1"
        await self.execute(sql, chat_id, execute=True)

    async def delete_bad_word(self, badword):
        sql = "DELETE FROM BadWords WHERE badword=$1"
        await self.execute(sql, badword, execute=True)

    async def drop_courses(self):
        await self.execute("DROP TABLE Courses", execute=True)