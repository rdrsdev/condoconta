from fastapi import APIRouter
from app.banking_account import account_controller

router = APIRouter()

router.include_router(account_controller.router, tags=[
    "Consult bank account"], prefix="/account")
