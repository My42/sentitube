from datetime import datetime

from pydantic import BaseModel


class YoutubeComment(BaseModel):
    id: str
    video_id: str
    like_count: int
    text: str
    updated_at: datetime
    published_at: datetime
