import os

import psycopg2

from server.src.models.analyze import Analyze


class AnalyzeRepository:
    def save(self, analyzes: list[Analyze]) -> None:
        conn = self.__get_conn()
        cur = conn.cursor()
        query = """
        INSERT INTO analyzes (justification, sentiment_score, yt_comment_id, yt_comment_text)
        VALUES (%s, %s, %s, %s)
        """

        try:
            cur.executemany(query, [analyze.model_dump() for analyze in analyzes])
            conn.commit()
        except Exception as e:
            conn.rollback()
        finally:
            cur.close()
            conn.close()

    def __get_conn(self):
        return psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host="postgres",
            port="5432",
        )
