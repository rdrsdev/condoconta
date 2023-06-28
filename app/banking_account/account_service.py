import datetime

from .account_entity import CheckBalance, Transfer
from .account_model import db


async def check_balance(data_baking: CheckBalance):
    for banking in db:
        if (banking.agency == data_baking.agency and banking.document == data_baking.document and
                banking.account_number == data_baking.account_number and
                banking.account_digit == data_baking.account_digit and
                banking.type == data_baking.type):
            return banking or {"message": "No transactions found"}


async def check_statement_account(data_baking: CheckBalance):
    current_month = datetime.datetime.now().month

    for banking in db:
        if (banking.agency == data_baking.agency and banking.document == data_baking.document and
                banking.account_number == data_baking.account_number and
                banking.account_digit == data_baking.account_digit and
                banking.type == data_baking.type) and banking.date.month == current_month:
            return banking or {"message": "No transactions found"}


async def transfer_balance(data_transfer: Transfer):
    await check_ownership(data_transfer.account_from.document, data_transfer.account_to.document)

    result_check_balance_from = await check_balance(data_transfer.account_from)

    await check_limit_balance(data_transfer.account_from.balance, result_check_balance_from.balance)

    result_check_balance_to = await check_balance(data_transfer.account_to)
    result_check_balance_to.balance += data_transfer.account_from.balance
    result_check_balance_to.date = datetime.datetime.now()

    result_check_balance_from.balance -= data_transfer.account_from.balance
    result_check_balance_from.date = datetime.datetime.now()

    return result_check_balance_to


async def check_ownership(from_document: str, to_document: str):
    if from_document != to_document:
        return {'The accounts are not owned by the same'}


async def check_limit_balance(desired_value: float, current_value: float):
    if current_value < desired_value:
        return {'You dont have enough balance for this transaction'}
