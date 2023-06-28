import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class AccountType(str, Enum):
    cc = "checking_account"
    cp = "savings_account"


class BankStatement(BaseModel):
    id: Optional[UUID] = uuid4()
    agency: int
    document: str
    account_number: int
    account_digit: int
    type: AccountType
    date: datetime.datetime
    description: str
    transaction_value: float
    balance: float


class BankStatementBalance(BaseModel):
    date: datetime.datetime
    description: str
    transaction_value: float
    balance: float


class CheckBalance(BaseModel):
    agency: int
    document: str
    account_number: int
    account_digit: int
    type: AccountType


class TransferFrom(BaseModel):
    agency: int
    document: str
    account_number: int
    account_digit: int
    type: AccountType
    balance: float


class TransferTo(BaseModel):
    agency: int
    document: str
    account_number: int
    account_digit: int
    type: AccountType


class Transfer(BaseModel):
    account_from: TransferFrom
    account_to: TransferTo
