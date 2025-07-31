from threading import Thread
import time

from web.app import create_app
from bot.bot import start_bot

app = create_app()

def run_flask():
    app.run(debug=False, host='0.0.0.0', port=8080)

def run_bot():
    start_bot()

if __name__ == "__main__":
    t1 = Thread(target=run_flask)
    t2 = Thread(target=run_bot)
    t1.start()
    time.sleep(2)
    t2.start()
