from core.celery import app
from time import sleep

@app.task
def test_task(d=20):
    sleep(d)
    print("test task was executed successfully!")
    return d*2