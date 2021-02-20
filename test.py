from flask import Flask
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = APScheduler()

times = 0

def scheduleTask():
    global times
    times += 1
    print("This test runs every",times ,"seconds")

if __name__ == '__main__':
    scheduler.add_job(id = 'Scheduled Task', func=scheduleTask, trigger="interval", seconds=1)
    scheduler.start()
    app.run(host="0.0.0.0")