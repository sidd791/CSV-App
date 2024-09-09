from celery import shared_task
from time import sleep

@shared_task
def add(a, b):
    sleep(5)
    return a + b

@shared_task
def clear_cache(id):
    print(f"Session cleared : {id}")
    return id