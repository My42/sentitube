import asyncio

from celery.app.task import Task
from injector import Injector
from src.services.sentiment_analyzer_service import SentimentAnalyserService
from src.worker import celery_app

injector = Injector()


@celery_app.task
def analyze_comments(yt_video_id: str) -> list[dict]:
    async def inner_fn(yt_video_id: str) -> list[dict]:
        sentiment_analyzer = injector.get(SentimentAnalyserService)

        comments = await sentiment_analyzer.analyze_comments(yt_video_id)

        return comments

    return asyncio.run(inner_fn(yt_video_id))


analyze_comments: Task = analyze_comments
