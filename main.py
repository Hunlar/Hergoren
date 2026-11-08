import asyncio
import logging

from pytgcalls import idle

from driver.veez import bot, call_py, user

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


async def start_bot():
    logger.info("Starting Telegram bot client")
    await bot.start()

    try:
        logger.info("Starting PyTgCalls / assistant client")
        await call_py.start()
        logger.info("Bot is ready")
        await idle()
    finally:
        logger.info("Stopping clients")
        try:
            await call_py.stop()
        except Exception:
            logger.exception("Error while stopping PyTgCalls")
        try:
            await user.stop()
        except Exception:
            logger.exception("Error while stopping assistant client")
        try:
            await bot.stop()
        except Exception:
            logger.exception("Error while stopping bot client")


if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        logger.info("Shutdown requested")
