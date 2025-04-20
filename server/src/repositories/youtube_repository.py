import os
from datetime import datetime

import httpx
from src.formatters.dict_keys_to_snake_case import dict_keys_to_snake_case
from src.models.youtube_comment import YoutubeComment
from src.models.youtube_comments_response import YoutubeCommentsResponse
from src.models.youtube_video import YoutubeVideo
from src.models.youtube_video_response import YoutubeVideoResponse


class YoutubeRepository:
    def __init__(self):
        self.__client = httpx.AsyncClient(
            base_url="https://www.googleapis.com/youtube/v3",
            headers={"X-goog-api-key": os.environ["YOUTUBE_ACCESS_TOKEN"]},
        )

    async def get_comments_by_video_id(
        self,
        video_id: str,
        count: int,
        part: str = "id,snippet",
        text_format: str = "plainText",
    ) -> list[YoutubeComment]:
        """
        Retrieves comments for a specific YouTube video.
        Args:
            video_id (str): The ID of the YouTube video to get comments from.
            count (int): The maximum number of comments to retrieve.
            part (str, optional): The parts of the comment to retrieve. Defaults to "id,snippet".
            text_format (str, optional): The format of the comment text. Defaults to "plainText".

        Returns:
            list[Comment]: A list of Comment objects containing the video comments.
        """
        params = {
            "maxResults": count,
            "part": part,
            "textFormat": text_format,
            "videoId": video_id,
        }

        comments = []
        next_page_token = None
        while len(comments) < count:
            response = await self.__client.get(
                "/commentThreads", params={**params, "pageToken": next_page_token}
            )
            json = dict_keys_to_snake_case(response.json())
            yt_response = YoutubeCommentsResponse(**json)

            comments.extend(
                [
                    YoutubeComment(
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
                    for item in yt_response.items
                ]
            )

            next_page_token = yt_response.next_page_token

            if next_page_token is None:
                break

        return comments

    async def get_video_by_id(
        self,
        id: str,
        part: str = "snippet, statistics",
    ) -> YoutubeVideo:
        """
        Retrieves information about a specific YouTube video.

        Args:
            id (str): The ID of the YouTube video to retrieve.
            part (str, optional): The parts of the video information to retrieve. Defaults to "snippet, statistics".

        Returns:
            YoutubeVideo: A YoutubeVideo object containing the video information.
        """
        params = {"part": part, "id": id}

        response = await self.__client.get("/videos", params=params)
        yt_response = YoutubeVideoResponse(
            **dict_keys_to_snake_case(response.json()["items"][0])
        )
        video = YoutubeVideo(
            description=yt_response.snippet.description,
            published_at=yt_response.snippet.published_at,
            tags=yt_response.snippet.tags,
            title=yt_response.snippet.title,
        )

        return video
