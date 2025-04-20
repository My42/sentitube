import os

from celery import Celery

celery_app = Celery(
    "sentiment-analyzer",
    broker=f"redis://{os.environ["REDIS_URL"]}",
    backend=f"redis://{os.environ["REDIS_URL"]}",
    include=["src.tasks.add"],
)

if __name__ == "__main__":
    celery_app.start()
