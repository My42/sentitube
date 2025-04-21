import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "sentiment-analyzer",
    broker=f"redis://{os.environ["REDIS_URL"]}",
    backend=f"redis://{os.environ["REDIS_URL"]}",
    include=["src.tasks.add", "src.tasks.analyze_comments"],
)

if __name__ == "__main__":
    celery_app.start()
