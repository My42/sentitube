from celery.result import AsyncResult
from dotenv import load_dotenv
from injector import Injector
from src.models.youtube_comment import YoutubeComment
from src.models.youtube_video import YoutubeVideo
from src.repositories.youtube_repository import YoutubeRepository
from src.tasks.analyze_comments import analyze_comments

load_dotenv()

from fastapi import FastAPI

app = FastAPI()
injector = Injector()


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


@app.get("/tasks/{task_id}")
async def get_task(task_id: str) -> dict:
    result = AsyncResult(task_id)

    return {
        "status": result.state,
        "result": result.result,
    }


@app.post("yt-video/analyze/{yt_video_id}")
async def analyze_sentiments_of_video(video_id: str) -> dict:
    task = analyze_comments.delay(video_id)

    return {"task_id": task.id}


@app.get("yt-video/analyze/{yt_video_id}")
async def get_video_analyze(video_id: str) -> dict:
    return {}
