from celery.result import AsyncResult
from dotenv import load_dotenv
from injector import Injector
from src.models.requests.post_yt_video_analyze import PostBodyYtVideoAnalyze
from src.repositories.analyze_repository import AnalyzeRepository
from src.tasks.analyze_comments import analyze_comments

load_dotenv()

from fastapi import FastAPI

app = FastAPI()
injector = Injector()


@app.get("/tasks/{task_id}")
async def get_task(task_id: str) -> dict:
    result = AsyncResult(task_id)

    return {
        "status": result.state,
        "result": result.result,
    }


@app.post("/yt-videos/analyze")
async def analyze_sentiments_of_video(body: PostBodyYtVideoAnalyze) -> dict:
    task = analyze_comments.delay(body.yt_video_id)

    return {"task_id": task.id}


@app.get("/yt-videos/{yt_video_id}/analyze")
async def get_video_analyze(yt_video_id: str) -> list:
    analyze_repo = injector.get(AnalyzeRepository)

    # TODO: Add pagination
    analyzes = await analyze_repo.get_by_yt_video_id(yt_video_id)

    return [analyze.model_dump() for analyze in analyzes]
