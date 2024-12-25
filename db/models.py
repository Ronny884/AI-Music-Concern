from datetime import datetime
from sqlalchemy import Table, Integer, String, MetaData, Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base


class CompaniesORM(Base):
    __tablename__ = 'companies'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    area: Mapped[str]
    website: Mapped[str]
    instagram: Mapped[str]
    telegram: Mapped[str]
    linkedin: Mapped[str]
    song_text: Mapped[str]
    song_path: Mapped[str]
    all_info: Mapped[str]
    vimeo_link: Mapped[str]
    cloudinary_link: Mapped[str]
    logs: Mapped[str]
    status: Mapped[str]


class EmailsORM(Base):
    __tablename__ = 'emails'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey(CompaniesORM.id, ondelete='CASCADE'))


class MessagesORM(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    content_type: Mapped[str]
    sent_by_me: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    thread_id: Mapped[str]
    goodai_related_email: Mapped[str]
    email_id: Mapped[int] = mapped_column(Integer, ForeignKey(EmailsORM.id, ondelete='CASCADE'))




