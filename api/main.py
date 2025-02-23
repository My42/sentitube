from dotenv import load_dotenv
from injector import Injector

from models.comment import Comment
from models.youtube_video import YoutubeVideo
from repositories.youtube_repository import YoutubeRepository

load_dotenv()

from fastapi import FastAPI

app = FastAPI()
injector = Injector()


@app.get("/analyze/{video_id}")
async def root(video_id: str):
    yt = injector.get(YoutubeRepository)

    # TODO: check if data in DB

    # TODO: Get video's data
    comments = await yt.get_comments_by_video_id(video_id, count=10)
    # TODO: Save video & comments data in DB
    # TODO: Analyze sentiments

    return {"message": "Done !"}


@app.get("/videos/{id}")
async def get_video_by_id(id: str) -> YoutubeVideo:
    yt = injector.get(YoutubeRepository)

    video = await yt.get_video_by_id(id)

    return video


@app.get("/videos/{id}/comments")
async def get_comments_by_video_id(id: str) -> list[Comment]:
    yt = injector.get(YoutubeRepository)

    comments = await yt.get_comments_by_video_id(id, 100)

    return comments
