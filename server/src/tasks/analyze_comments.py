import asyncio

from celery.app.task import Task
from injector import Injector
from src.models.analyze import Analyze
from src.services.sentiment_analyzer_service import SentimentAnalyserService
from src.repositories.analyze_repository import AnalyzeRepository
from src.worker import celery_app

injector = Injector()


@celery_app.task(bind=True)
def analyze_comments(self, yt_video_id: str) -> list[dict]:
    async def inner_fn(yt_video_id: str) -> list[dict]:
        self.update_state(state='PROGRESS', meta={'status': 'Fetching video and comments'})

        sentiment_analyzer = injector.get(SentimentAnalyserService)
        analyze_repository = injector.get(AnalyzeRepository)

        comments = await sentiment_analyzer.analyze_comments(yt_video_id)
        
        self.update_state(state='PROGRESS', meta={'status': 'Saving analysis results'})
        await analyze_repository.save(comments)

        return [comment.model_dump() for comment in comments]

    return asyncio.run(inner_fn(yt_video_id))


analyze_comments: Task = analyze_comments
