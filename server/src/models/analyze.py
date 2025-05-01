from pydantic import BaseModel


class Analyze(BaseModel):
    justification: str
    sentiment_score: float
    yt_comment_id: str
    yt_comment_text: str
    yt_video_id: str
