import os

import httpx

from formatters.dict_keys_to_snake_case import dict_keys_to_snake_case
from models.youtube_comments_response import YoutubeCommentsResponse
from models.youtube_video import YoutubeVideo
from models.youtube_video_response import YoutubeVideoResponse


class YoutubeRepository:
    def __init__(self):
        self.__client = httpx.AsyncClient(
            base_url="https://www.googleapis.com/youtube/v3",
            headers={"X-goog-api-key": os.environ["YOUTUBE_ACCESS_TOKEN"]},
        )

    async def get_comments_by_video_id(
        self,
        video_id: str,
        max_results: int = 100,
        part: str = "id,snippet",
        text_format: str = "plainText",
        next_page_token: str | None = None,
    ) -> YoutubeCommentsResponse:
        params = {
            "maxResults": max_results,
            "part": part,
            "textFormat": text_format,
            "videoId": video_id,
        }

        if next_page_token is not None:
            params["pageToken"] = next_page_token

        response = await self.__client.get("/commentThreads", params=params)
        json = dict_keys_to_snake_case(response.json())
        yt_response = YoutubeCommentsResponse(**json)

        return yt_response

    async def get_video_by_id(
        self,
        id: str,
        part: str = "snippet, statistics",
    ) -> YoutubeVideo:
        params = {"part": part, "id": id}

        response = await self.__client.get("/videos", params=params)
        yt_response = YoutubeVideoResponse(
            **dict_keys_to_snake_case(response.json()["items"][0])
        )
        yt_video = YoutubeVideo(
            description=yt_response.snippet.description,
            published_at=yt_response.snippet.published_at,
            tags=yt_response.snippet.tags,
            title=yt_response.snippet.title,
        )

        return yt_video
