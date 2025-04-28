import asyncio

from celery.app.task import Task
from src.repositories.youtube_repository import YoutubeRepository
from src.services.sentiment_analyzer_service import SentimentAnalyserService
from src.worker import celery_app


@celery_app.task
def analyze_comments(video_id: str) -> list[dict]:
    async def inner_fn(video_id: str) -> list[dict]:
        yt = YoutubeRepository()
        sentiment_analyzer = SentimentAnalyserService()

        yt_video = await yt.get_video_by_id(video_id)
        yt_comments = await yt.get_comments_by_video_id(video_id, count=10)
        comments = await sentiment_analyzer.analyze_comments(yt_video, yt_comments)
        return comments

    return asyncio.run(inner_fn(video_id))


analyze_comments: Task = analyze_comments
