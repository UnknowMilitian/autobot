import asyncpg
import config


class DBManager:
    def __init__(self):
        self.pool = None

    async def connect(self):
        """Connect to the database"""
        self.pool = await asyncpg.create_pool(connect=config.DB_DNS)

    async def disconnect(self):
        """Disconnect to the database"""
        if self.pool is not None:
            await self.pool.close()

    async def fetch(self, query: str, *args):
        """Fetch a list of objects from the database"""
        async with self.pool.acquire() as connection:
            results = await connection.fetch(query, *args)
            return [dict(results) for result in results]

    async def fetch_one(self, query: str, *args):
        """Fetch a single object from the database"""
        async with self.pool.acquire() as connection:
            result = await connection.fetchrow(query, *args)
            return dict(result)

    async def execute(self, query, *args):
        """Execute a SQL command"""
        async with self.pool.acquire() as connection:
            await connection.execute(query, *args)


db = DBManager()
