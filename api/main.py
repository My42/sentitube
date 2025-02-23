from dotenv import load_dotenv
from injector import Injector

from services.youtube_service import YoutubeService

load_dotenv()

from fastapi import FastAPI

app = FastAPI()
injector = Injector()


@app.get("/analyze/{video_id}")
async def root(video_id: str):
    yt = injector.get(YoutubeService)

    # TODO: check if data in DB

    # TODO: Get video's data
    comments = await yt.get_comments_by_video_id(video_id, count=10)
    # TODO: Save video & comments data in DB
    # TODO: Analyze sentiments

    return comments
