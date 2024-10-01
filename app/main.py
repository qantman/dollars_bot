import asyncio
from aiogram import Bot, Dispatcher
from app.config import Config
from app.handlers.start_handler import router as hello_router

async def main():
    bot = Bot(token=Config.token)
    db = Dispatcher()
    db.include_routers(
        hello_router
    )
    await db.start_polling(bot)

if __name__ == "__main__":
    print("TG bot has been started")
    Config.start_logger()
    asyncio.run(main())
