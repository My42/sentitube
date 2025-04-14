from dotenv import load_dotenv
from injector import Injector
from models.youtube_comment import YoutubeComment
from models.youtube_video import YoutubeVideo
from repositories.youtube_repository import YoutubeRepository
from services.sentiment_analyzer_service import SentimentAnalyserService

load_dotenv()

from fastapi import FastAPI

app = FastAPI()
injector = Injector()


@app.get("/analyze/{video_id}")
async def analyze_sentiments_of_video(video_id: str):
    yt = injector.get(YoutubeRepository)
    sentiment_analyzer = injector.get(SentimentAnalyserService)

    # TODO: check if data in DB

    yt_video = await yt.get_video_by_id(video_id)
    yt_comments = await yt.get_comments_by_video_id(video_id, count=10)
    comments = await sentiment_analyzer.analyze_comments(yt_video, yt_comments)
    # TODO: Save video & comments data in DB

    return comments


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
