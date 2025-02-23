from dotenv import load_dotenv

load_dotenv()

import os
from fastapi import FastAPI
from services.youtube_service import YoutubeService

app = FastAPI()

print("YOUTUBE_ACCESS_TOKEN =", os.environ.get("YOUTUBE_ACCESS_TOKEN", None))


@app.get("/analyze/{video_id}")
async def root(video_id: str):
    yt = YoutubeService()

    comments = await yt.get_comments_by_video_id(video_id)

    return {"comments": comments}
