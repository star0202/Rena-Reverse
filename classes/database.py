from logging import Logger

from aiosqlite import connect, Connection, Cursor


class Database:
    def __init__(self):
        self.path: str
        self.cursor = Cursor
        self.conn: Connection

    @classmethod
    async def create(cls, path: str, logger: Logger):
        self = Database()
        self.path = path
        self.conn = await connect(self.path, isolation_level=None)
        await self.conn.set_trace_callback(logger.info)
        self.cursor = await self.conn.cursor()
        return self

    async def insert(self, table: str, value: tuple):
        await self.cursor.execute(f"INSERT INTO {table} VALUES {value}")

    async def select(self, table: str, value_id: int) -> tuple | None:
        await self.cursor.execute(f"SELECT * FROM {table} WHERE id={value_id}")
        return await self.cursor.fetchone()

    async def update(self, table: str, column: str, value: str | bool | int, value_id: int):
        if isinstance(value, str):
            value = f"'{value}'"
        await self.cursor.execute(f"UPDATE {table} SET {column}={value} WHERE id={value_id}")

    async def delete(self, table: str, value_id: int):
        await self.cursor.execute(f"DELETE FROM {table} WHERE id={value_id}")

    async def execute(self, sql: str) -> tuple | None:
        await self.cursor.execute(sql)
        return await self.cursor.fetchone()
