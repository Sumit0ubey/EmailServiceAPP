from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from EmailServiceAPI.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    fullName = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    apiToken = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False, server_default=text("''"))
    isPaidUser = Column(Boolean, nullable=False, server_default=text('false'))
    numberOfEmailSend = Column(Integer, nullable=False, server_default=text("0"))
    numberOfEmailCanSend = Column(Integer, nullable=False, server_default=text("20"))
    defaultEmailTimeUsed = Column(Integer, nullable=False, server_default=text("0"))
    defaultEmailTimeCanUsed = Column(Integer, nullable=False, server_default=text("5"))
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, nullable=False)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    sendTo = Column(String, nullable=False)
    service = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user = relationship("User")


class DefaultEmail(Base):
    __tablename__ = "automaticEmail"
    id = Column(Integer, primary_key=True, nullable=False)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    sendTo = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user = relationship("User")
