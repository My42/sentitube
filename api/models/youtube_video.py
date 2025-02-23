from typing import Optional

from pydantic import BaseModel


class YoutubeVideo(BaseModel):
    published_at: str
    title: str
    description: str
    tags: Optional[list[str]] = None
