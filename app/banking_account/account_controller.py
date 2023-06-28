from typing import Union

from fastapi import APIRouter

from app.banking_account import account_service
from app.banking_account.account_entity import CheckBalance, BankStatementBalance, Transfer

router = APIRouter()


@router.post("/check-balance", response_model=Union[BankStatementBalance, dict])
async def check_total_balance(data_baking: CheckBalance):
    return await account_service.check_balance(data_baking)


@router.post("/transfer", response_model=BankStatementBalance)
async def transfer_balance(data_transfer: Transfer):
    return await account_service.transfer_balance(data_transfer)


@router.post("/check-statement-account", response_model=Union[BankStatementBalance, dict])
async def check_balance_of_month(data_baking: CheckBalance):
    return await account_service.check_statement_account(data_baking)
