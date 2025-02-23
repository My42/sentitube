import os

import httpx

from formatters.dict_keys_to_snake_case import dict_keys_to_snake_case
from models.youtube_comments_response import YoutubeCommentsResponse


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
    ) -> YoutubeCommentsResponse:
        params = {
            "maxResults": max_results,
            "part": part,
            "textFormat": text_format,
            "videoId": video_id,
        }

        response = await self.__client.get("/commentThreads", params=params)
        json = dict_keys_to_snake_case(response.json())
        yt_response = YoutubeCommentsResponse(**json)

        return yt_response
