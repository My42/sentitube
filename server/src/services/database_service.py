import os
from typing import Iterable, LiteralString

from psycopg import AsyncConnection


class DatabaseService:
    __conn: AsyncConnection

    async def query(self, q: LiteralString, params_seq: Iterable | None = None):
        conn = await self.__get_conn()

        async with conn.cursor() as cur:
            async with conn.transaction():
                if params_seq:
                    await cur.executemany(q, params_seq, returning=True)
                    try:
                        return await cur.fetchall()
                    except:
                        return []
                else:
                    await cur.execute(q)
                    try:
                        return [await cur.fetchone()]
                    except:
                        return []

    async def __get_conn(self) -> AsyncConnection:
        if getattr(self, "__con", None):
            return self.__conn

        self.__con = await AsyncConnection.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
        )

        return self.__con
