from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.configs.Config import mail_config
from typing import List


conf = ConnectionConfig(
    MAIL_USERNAME=mail_config["MAIL_USERNAME"],
    MAIL_PASSWORD=mail_config["MAIL_PASSWORD"],
    MAIL_FROM=mail_config["MAIL_FROM"],
    MAIL_PORT=mail_config["MAIL_PORT"],
    MAIL_SERVER=mail_config["MAIL_SERVER"],
    MAIL_TLS=mail_config["MAIL_TLS"],
    MAIL_SSL=mail_config["MAIL_SSL"],
    USE_CREDENTIALS=mail_config["USE_CREDENTIALS"],
    VALIDATE_CERTS=mail_config["VALIDATE_CERTS"]
)

async def send_email(subject: str, recipient: List, message: str):
    message = MessageSchema(
        subject=subject,
        recipients=recipient,
        body=message,
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})     

