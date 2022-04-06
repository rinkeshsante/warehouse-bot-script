from Bot import Bot
import time

URL = "http://127.0.0.1:8000/bot/api/next-task"

bot = Bot(22, 0, 0, URL)

while True:
    time.sleep(1)
    bot.getNewTask()
    bot.move()
    bot.showLocation()
