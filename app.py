from flask import Flask, render_template
from Classes.GenerateStory import *
from apscheduler.schedulers.background import BackgroundScheduler
import os
print('it works!')
app = Flask(__name__)

@app.route('/')
def home():
    k = D
    return render_template('index.html', d=k)

# @app.route('/about')
# def about():




if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # scheduler.add_job(func=to_app, trigger="interval", seconds=10000000)
    scheduler.add_job(func=to_app, trigger='interval', hours=3, start_date='2020-12-01 00:09:00', end_date='2100-06-15 11:00:00')
    scheduler.start()
   # port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)


