from flask import Flask, render_template
from Classes.GenerateStory import *
from apscheduler.schedulers.background import BackgroundScheduler
import os
print('it works!')
app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 01:15:01', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 01:15:02', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 01:15:03', end_date='2100-06-15 11:00:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 01:15:04', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 01:15:05', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 01:15:06', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 01:15:07', end_date='2100-06-15 11:00:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 01:15:08', end_date='2100-06-15 09:05:00')

scheduler.start()


@app.route('/')
def home():

    return render_template('home-page_demo.html',type=type,published = list(zip(IMAGE_TO_SLANDER,DATE,TITLE,ARTICLE)))

@app.template_global(name='zip')
def _zip(*args, **kwargs): #to not overwrite builtin zip in globals
    return __builtins__.zip(*args, **kwargs)


# if __name__ == '__main__':
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     app.run(debug=True)



