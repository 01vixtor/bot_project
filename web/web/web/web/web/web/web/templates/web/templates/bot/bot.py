from telegram import Bot
import time
import random
from config_loader import get_config
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")  # exemplo: -1001234567890

bot = Bot(token=TOKEN)

def start_bot():
    while True:
        config = get_config()
        if config:
            msg = config["message_text"]
            value = round(random.uniform(config["min"], config["max"]), 2)
            msg = msg.replace("{{valor}}", str(value))
            bot.send_message(chat_id=GROUP_ID, text=msg)
            time.sleep(config["interval"] * 60)
        else:
            time.sleep(60)

if __name__ == "__main__":
    start_bot()
