from typing import Optional

from pydantic import BaseModel


class Snippet(BaseModel):
    published_at: str
    channel_id: str
    title: str
    description: str
    channel_title: str
    tags: Optional[list[str]] = None


class YoutubeVideoResponse(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: Snippet
