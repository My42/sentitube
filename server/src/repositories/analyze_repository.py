from injector import inject
from src.models.analyze import Analyze
from src.services.database_service import DatabaseService


class AnalyzeRepository:
    @inject
    def __init__(self, database_service: DatabaseService) -> None:
        self.__database_service = database_service

    async def save(self, analyzes: list[Analyze]) -> list[str]:
        """
        Saves a list of Analyze objects to the database.

        Args:
            analyzes (list[Analyze]): A list of Analyze objects to be saved.

        Returns:
            list[str]: The list of YouTube comment IDs that have been saved.
        """
        query = f"""
        INSERT INTO analyzes (justification, sentiment_score, yt_comment_id, yt_comment_text, yt_video_id)
        VALUES (%(justification)s, %(sentiment_score)s, %(yt_comment_id)s, %(yt_comment_text)s, %(yt_video_id)s)
        """

        await self.__database_service.query(
            query,
            [analyze.model_dump() for analyze in analyzes],
        )

        return [analyze.yt_comment_id for analyze in analyzes]
