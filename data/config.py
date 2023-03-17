from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str('BOT_TOKEN') # Bot toekn
ADMINS = [6092600575] # adminlar ro'yxati #1435473812 #6092600575


DB_USER = env.str('DB_USER')
DB_PASS = env.str('DB_PASS')
DB_NAME = env.str('DB_NAME')
DB_HOST = env.str('DB_HOST')