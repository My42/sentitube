from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from repositories.youtube_repository import YoutubeRepository

app = FastAPI()


@app.get("/analyze/{video_id}")
async def root(video_id: str):
    yt = YoutubeRepository()

    comments = await yt.get_comments_by_video_id(video_id)

    return comments
