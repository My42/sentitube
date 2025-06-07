import os
from typing import Iterable, Literal, LiteralString

from psycopg import AsyncConnection, rows


class DatabaseService:
    __conn: AsyncConnection

    async def query(
        self,
        q: LiteralString,
        params: Iterable | None = None,
        execute_mode: Literal["many", "single"] = "single",
    ):
        conn = await self.__get_conn()

        async with conn.cursor(row_factory=rows.dict_row) as cur:
            async with conn.transaction():
                if execute_mode == "many":
                    if params is None:
                        raise ValueError(
                            "params_seq cannot be None when execute_mode is 'many'"
                        )
                    await cur.executemany(q, params)
                    try:
                        return await cur.fetchall()
                    except:
                        return []
                else:
                    await cur.execute(q, params)
                    try:
                        return await cur.fetchall()
                    except:
                        return []

    async def __get_conn(self) -> AsyncConnection:
        if getattr(self, "__conn", None):
            return self.__conn

        self.__conn = await AsyncConnection.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
        )

        return self.__conn
