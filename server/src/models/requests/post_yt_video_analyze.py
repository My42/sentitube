from pydantic import BaseModel


class PostBodyYtVideoAnalyze(BaseModel):
    yt_video_it: str
