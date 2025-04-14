from celery import Celery

celery_app = Celery(
    "sentiment-analyzer",
    broker="redis://localhost:6379",
    backend="redis://localhost:6379",
)


@celery_app.task
def add(x, y):
    """Simple Celery task to add two numbers."""
    return x + y
