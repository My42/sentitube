from celery.app.task import Task
from src.worker import celery_app


@celery_app.task
def add_task(x: int, y: int) -> int:
    """Simple Celery task to add two numbers."""
    return x + y


add_task: Task = add_task
