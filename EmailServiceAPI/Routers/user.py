import asyncio

from fastapi import APIRouter, status, Header, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from passlib.hash import bcrypt
from dotenv import load_dotenv
from os import getenv

from EmailServiceAPI.Controller.writer import sendMail
from EmailServiceAPI.schema import CreateUserSchema, GetUserSchema, SecureAccount, Data
from EmailServiceAPI.database import get_db
from EmailServiceAPI.models import User
from EmailServiceAPI.utils import generate_key, hashPassword


load_dotenv()

EMAIL = getenv('SYSTEM_EMAIL')
PASSKEY = getenv('SYSTEM_EMAIL_PASSKEY')

router = APIRouter(prefix="/users", tags=["User"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register(user: CreateUserSchema, db: AsyncSession = Depends(get_db)):
    key = generate_key()
    new_user = User(apiToken=key, password=hashPassword(""), **user.dict())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    is_email_send = await asyncio.to_thread(sendMail, username=EMAIL, password=PASSKEY, _to=new_user.email,
                                            subject="Welcome to Email Service API - Registration Successful",
                                            data="", template_id=5, iD=new_user.id, token=new_user.apiToken)

    if not is_email_send:
        raise HTTPException(status_code=500, detail="Failed to send email")

    return {"Message": "We have send your credential to your email please check it.."}


@router.get("/info", status_code=status.HTTP_302_FOUND, response_model=GetUserSchema)
async def info(token: str = Header(...), db: AsyncSession = Depends(get_db)):
    user = await db.execute(select(User).where(User.apiToken == token))
    user = user.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Token")

    return GetUserSchema(fullName=user.fullName, email=user.email, apiToken=user.apiToken, isPaidUser=user.isPaidUser, numberOfEmailSend=user.numberOfEmailSend, createdAt=user.createdAt)


@router.get("/upgrade", status_code=status.HTTP_200_OK)
async def becomePaidUser(token: str = Header(...), db: AsyncSession = Depends(get_db)):
    user = await db.execute(select(User).where(User.apiToken == token))
    user = user.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Token")

    is_email_send = await asyncio.to_thread(sendMail, username=EMAIL, password=PASSKEY, _to=user.email, subject="Your Upgrade Plan - increase your email quota",
                                            data="", template_id=4)

    if not is_email_send:
        raise HTTPException(status_code=500, detail="Failed to send email")

    return {"Message": "We have send you an email please check it.."}


@router.post("/newToken/{id}", status_code=status.HTTP_202_ACCEPTED)
async def newToken(id: int, data: Data, token: str = Header(...), db: AsyncSession = Depends(get_db)):
    user = await db.execute(select(User).where(and_(User.id == id, User.apiToken == token)))
    user = user.scalar_one_or_none()

    if not user and not bcrypt.verify(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Attempt of Unauthorized Access")

    key = generate_key()
    user.apiToken = key
    await db.commit()
    await db.refresh(user)

    is_email_send = await asyncio.to_thread(sendMail, username=EMAIL,
                                            password=PASSKEY, _to=user.email,
                                            subject="Email Service API - Token Changed Successful",
                                            data="", template_id=6, token=user.apiToken)

    if not is_email_send:
        raise HTTPException(status_code=500, detail="Failed to send email")

    return {"Message": "We have send you an email with your new token please check it.."}


@router.put("/secureAccount{id}", status_code=status.HTTP_202_ACCEPTED)
async def setPassword(id: int, data: SecureAccount, token: str = Header(...), db: AsyncSession = Depends(get_db)):
    if data.setPassword != data.confirmPassword:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Mis-Match - Password should be same")

    user = await db.execute(select(User).where(and_(User.id == id, User.apiToken == token, User.email == data.email)))
    user = user.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Attempt of Unauthorized Access")

    user.password = hashPassword(data.setPassword)
    await db.commit()
    await db.refresh(user)

    return JSONResponse(content={"message": "Now your Account is Secure | Password is set"}, status_code=202)
