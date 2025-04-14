from typing import Optional

from pydantic import BaseModel


class AuthorChannelId(BaseModel):
    value: str


class CommentSnippet(BaseModel):
    channel_id: str
    video_id: str
    text_display: str
    text_original: str
    author_display_name: str
    author_profile_image_url: str
    author_channel_url: str
    author_channel_id: AuthorChannelId
    can_rate: bool
    viewer_rating: str
    like_count: int
    published_at: str
    updated_at: str


class TopLevelComment(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: CommentSnippet


class CommentThreadSnippet(BaseModel):
    channel_id: str
    video_id: str
    top_level_comment: TopLevelComment
    can_reply: bool
    total_reply_count: int
    is_public: bool


class CommentThread(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: CommentThreadSnippet


class PageInfo(BaseModel):
    total_results: int
    results_per_page: int


class YoutubeCommentsResponse(BaseModel):
    kind: str
    etag: str
    next_page_token: Optional[str]
    page_info: PageInfo
    items: list[CommentThread]
