import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy import URL, create_engine, text
from config.config_reader import settings


db_url = settings.DB_URL

async_engine = create_async_engine(
    url=db_url,
    echo=False
)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass


class TableCreator:
    @staticmethod
    async def create_table_companies():
        query = """
        CREATE TABLE IF NOT EXISTS companies (
        id SERIAL PRIMARY KEY,
        name TEXT,
        area TEXT,
        website TEXT,
        instagram TEXT,
        telegram TEXT,
        linkedin TEXT,
        song_text TEXT,
        song_path TEXT,
        all_info TEXT,
        vimeo_link TEXT,
        cloudinary_link TEXT,
        logs TEXT,
        status TEXT
        );
        """
        async with async_engine.begin() as conn:
            await conn.execute(text(query))

    @staticmethod
    async def create_table_emails():
        query = """
            CREATE TABLE IF NOT EXISTS emails (
            id SERIAL PRIMARY KEY,
            email TEXT,
            company_id INT,
            FOREIGN KEY (company_id) REFERENCES companies (id)

            );
            """
        async with async_engine.begin() as conn:
            await conn.execute(text(query))

    @staticmethod
    async def create_table_messages():
        query = """
                CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                content TEXT,
                content_type TEXT,
                sent_by_me BOOLEAN,
                created_at TIMESTAMP,
                thread_id TEXT,
                goodai_related_email TEXT,
                email_id INT,
                FOREIGN KEY (email_id) REFERENCES emails (id)

                );
                """
        async with async_engine.begin() as conn:
            await conn.execute(text(query))













# class TableCreator:
#     @staticmethod
#     async def create_table_company():
#         query = """
#         CREATE TABLE IF NOT EXISTS company (
#         id SERIAL PRIMARY KEY,
#         name TEXT,
#         website TEXT,
#         email TEXT[],
#         instagram TEXT,
#         telegram TEXT,
#         linkedin TEXT,
#         song_text TEXT,
#         song_link_1 TEXT,
#         song_link_2 TEXT,
#         area TEXT,
#         message TEXT,
#         all_info TEXT,
#         status TEXT
#         );
#         """
#         async with async_engine.begin() as conn:
#             await conn.execute(text(query))


# if __name__ == '__main__':
#     asyncio.run(TableCreator.create_table_companies())
