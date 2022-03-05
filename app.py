from utils.set_bot_commands import set_default_commands
from loader import db
from asyncpg.exceptions import PostgresSyntaxError


async def on_startup(dp):

    await db.create()
    await db.create_table_users()

    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
