from sqlalchemy import Column, Integer, BigInteger, String, DateTime, func
from .db import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True, nullable=False)
    fullname = Column(String)
    username = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
