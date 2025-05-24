from fastapi import APIRouter, status, Header, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from dotenv import load_dotenv
from os import getenv
import asyncio

from EmailServiceAPI.schema import EmailSchema, EmailWithPasskey
from EmailServiceAPI.database import get_db
from EmailServiceAPI.models import User, Email, DefaultEmail
from EmailServiceAPI.Controller.writer import sendMail
from EmailServiceAPI.utils import get_email_service

load_dotenv()

EMAIL = getenv('SYSTEM_EMAIL')
PASSKEY = getenv('SYSTEM_EMAIL_PASSKEY')

router = APIRouter(prefix="/email", tags=["Email_Service"])


@router.post("/", status_code=status.HTTP_202_ACCEPTED)
async def sendEmail(email: EmailWithPasskey, token: str = Header(...), db: AsyncSession = Depends(get_db),
                    company_name: str = None, company_link: str = None, email_title: str = None, template_id: int = 0):
    user = await db.execute(select(User).where(User.apiToken == token))
    user = user.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")

    if user.numberOfEmailSend > user.numberOfEmailCanSend:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Maximum quota exceeded")

    service = get_email_service(user.email)

    is_email_send = await asyncio.to_thread(sendMail, user.email, email.passKey, email.sendTo, email.title,
                                            email.content, template_id, company_name, company_link, email_title)

    if not is_email_send:
        raise HTTPException(status_code=500, detail="Failed to send email... Check your credential and try again.")

    user.numberOfEmailSend += 1
    new_email = Email(userId=user.id, service=service, sendTo=email.sendTo)
    db.add(new_email)
    await db.commit()
    await db.refresh(new_email)
    content = {
        "Message": f"Email send to {new_email.sendTo} with tile {email.title} using {new_email.service} service"}
    return JSONResponse(content=content, status_code=202)


@router.post("/default", status_code=status.HTTP_202_ACCEPTED)
async def defaultEmailService(email: EmailSchema, token: str = Header(...), db: AsyncSession = Depends(get_db),
                              company_name: str = None, company_link: str = None, email_title: str = None,
                              template_id: int = 0):
    user = await db.execute(select(User).where(User.apiToken == token))
    user = user.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail not found")

    if user.numberOfEmailSend >= user.numberOfEmailCanSend or user.defaultEmailTimeUsed >= user.defaultEmailTimeCanUsed:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Maximum quota exceeded")

    is_email_send = await asyncio.to_thread(sendMail, EMAIL, PASSKEY, email.sendTo,
                                            email.title,
                                            email.content, template_id, company_name, company_link, email_title)
    if not is_email_send:
        raise HTTPException(status_code=500, detail="Failed to send email... Check your credential and try again.")

    user.numberOfEmailSend += 1
    user.defaultEmailTimeUsed += 1
    new_email = DefaultEmail(userId=user.id, sendTo=email.sendTo)
    db.add(new_email)
    await db.commit()
    await db.refresh(new_email)
    content = {
        "Message": f"Email send to {new_email.sendTo} with tile {email.title} using Gmail service"}
    return JSONResponse(content=content, status_code=202)
