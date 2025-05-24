from pydantic import BaseModel, EmailStr, field_serializer
from datetime import datetime
from typing import Optional

from EmailServiceAPI.utils import serialize_timestamp


class CreateUserSchema(BaseModel):
    fullName: str
    email: EmailStr


class GetUserSchema(BaseModel):
    fullName: str
    email: EmailStr
    apiToken: str
    isPaidUser: bool
    numberOfEmailSend: int
    createdAt: datetime

    @field_serializer("createdAt")
    def timestampSerializer(self, dt: datetime) -> str:
        return serialize_timestamp(dt)

    class Config:
        from_attributes = True


class EmailSchema(BaseModel):
    title: str
    content: str
    sendTo: EmailStr


class EmailWithPasskey(EmailSchema):
    passKey: str


class SecureAccount(BaseModel):
    email: EmailStr
    setPassword: str
    confirmPassword: str

    class Config:
        from_attributes = True


class Data(BaseModel):
    password: Optional[str] = ""

