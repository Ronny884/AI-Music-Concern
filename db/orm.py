import asyncio
import logging
from sqlalchemy import text, select, delete, distinct
from sqlalchemy import and_, or_
from db.database import *
from db.models import *


# нестрогое добавление компании
async def insert_company_lax(**kwargs):
    try:
        async with async_session_factory() as session:
            company = CompaniesORM(**kwargs)
            session.add(company)
            await session.flush()
            company_id = company.id
            await session.commit()
            return company_id
    except Exception as e:
        logging.error(e)
        return None


# добавление email
async def insert_email(email: str, company_id: int):
    try:
        async with async_session_factory() as session:
            new_email = EmailsORM(email=email, company_id=company_id)
            session.add(new_email)
            await session.flush()
            mail_id = new_email.id
            await session.commit()
            return mail_id
    except Exception as e:
        logging.error(e)
        return None


# добавление сообщения
async def insert_message(content: str, content_type: str, sent_by_me: bool, goodai_related_email: str,
                         email_id: int, thread_id: str = None):
    try:
        async with async_session_factory() as session:
            new_message = MessagesORM(
                content=content,
                content_type=content_type,
                sent_by_me=sent_by_me,
                created_at=datetime.utcnow(),
                thread_id=thread_id,
                happyai_related_email=goodai_related_email,
                email_id=email_id
            )
            session.add(new_message)
            await session.commit()
    except Exception as e:
        logging.error(e)
        return None


# проверка, есть ли организация уже в базе
async def company_exists_in_db(name):
    try:
        async with async_session_factory() as session:
            stmt = select(CompaniesORM).where(CompaniesORM.name == name)
            result = await session.execute(stmt)
            company = result.scalars().first()
            return company is not None
    except Exception as e:
        logging.error(e)
        return False




