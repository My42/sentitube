from celery.result import AsyncResult
from dotenv import load_dotenv
from injector import Injector
from openai import BaseModel
from src.models.youtube_comment import YoutubeComment
from src.models.youtube_video import YoutubeVideo
from src.repositories.youtube_repository import YoutubeRepository
from src.services.sentiment_analyzer_service import SentimentAnalyserService
from src.tasks.add import add_task
from src.tasks.analyze_comments import analyze_comments

load_dotenv()

from fastapi import FastAPI

app = FastAPI()
injector = Injector()


# @app.get("/analyze/{video_id}")
# async def analyze_sentiments_of_video(video_id: str):
#     yt = injector.get(YoutubeRepository)
#     sentiment_analyzer = injector.get(SentimentAnalyserService)

#     # TODO: check if data in DB

#     yt_video = await yt.get_video_by_id(video_id)
#     yt_comments = await yt.get_comments_by_video_id(video_id, count=10)
#     comments = await sentiment_analyzer.analyze_comments(yt_video, yt_comments)
#     # TODO: Save video & comments data in DB

#     return comments


@app.get("/videos/{id}")
async def get_video_by_id(id: str) -> YoutubeVideo:
    yt = injector.get(YoutubeRepository)

    yt_video = await yt.get_video_by_id(id)

    return yt_video


@app.get("/videos/{id}/comments")
async def get_comments_by_video_id(id: str) -> list[YoutubeComment]:
    yt = injector.get(YoutubeRepository)

    yt_comments = await yt.get_comments_by_video_id(id, 100)

    return yt_comments


class AddBody(BaseModel):
    a: int
    b: int


@app.post("/add")
def call_add(body: AddBody) -> dict:
    """Trigger 'add' Celery task"""
    task = add_task.delay(body.a, body.b)
    return {"task_id": task.id}


@app.get("/tasks/{task_id}")
async def get_task(task_id: str) -> dict:
    result = AsyncResult(task_id)

    return {
        "status": result.state,
        "result": result.result,
    }


@app.get("/analyze/{video_id}")
async def analyze_sentiments_of_video(video_id: str) -> dict:
    task = analyze_comments.delay(video_id)
    return {"task_id": task.id}
