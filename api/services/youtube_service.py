from datetime import datetime

from injector import inject

from models.comment import Comment
from repositories.youtube_repository import YoutubeRepository


class YoutubeService:
    @inject
    def __init__(self, yt_repository: YoutubeRepository) -> None:
        self.__yt_repository = yt_repository

    async def get_comments_by_video_id(
        self, video_id: str, count: int
    ) -> list[Comment]:
        comments: list[Comment] = []
        next_page_token = None

        while len(comments) != count:
            response = await self.__yt_repository.get_comments_by_video_id(
                video_id,
                max_results=count,
                next_page_token=next_page_token,
            )
            comments.extend(
                [
                    Comment(
                        id=item.id,
                        video_id=item.snippet.video_id,
                        like_count=item.snippet.top_level_comment.snippet.like_count,
                        text=item.snippet.top_level_comment.snippet.text_display,
                        published_at=datetime.fromisoformat(
                            item.snippet.top_level_comment.snippet.published_at
                        ),
                        updated_at=datetime.fromisoformat(
                            item.snippet.top_level_comment.snippet.updated_at
                        ),
                    )
                    for item in response.items
                ]
            )

            next_page_token = response.next_page_token

        return comments
