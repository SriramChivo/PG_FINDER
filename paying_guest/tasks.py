from os import name
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask
from celery.decorators import task
from config.celery import app


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, add.s(10, 10), name='sum_of_two_numbers')

@task(name="normal task")
def normal():
    return "Regular one"


@app.task
def add(x, y):
    return x+y


@app.task
def bro(string):
    return str(string)


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'tasks.add',
        'schedule': 5.0,
        'args': (16, 16)
    },
    'add-every-10-seconds': {
        'task': 'tasks.bro',
        'schedule': 10.0,
        'args': ("Bro great after 10 seconds")
    },
}
app.conf.timezone = 'UTC'

# @PeriodicTask(run_every=(crontab(minute='*/1')), name="periodic")
# def period():
#     return "Triggered every minute"

# normal.delay()
