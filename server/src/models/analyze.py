from typing import Optional
from pydantic import BaseModel


class Analyze(BaseModel):
    justification: str
    sentiment_score: Optional[float] = None
    yt_comment_id: str
    yt_comment_text: str
    yt_video_id: str
