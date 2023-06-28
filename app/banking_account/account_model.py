from typing import List

from app.banking_account.account_entity import BankStatement

db: List[BankStatement] = [
    BankStatement(
        id='c86c8a0e-a451-454b-be20-81e6edaf8524',
        document='123456789011',
        agency=1233,
        account_number=90102,
        account_digit=2,
        type='checking_account',
        date='2023-05-06 00:00:00',
        description="Transferência para conta corrente",
        transaction_value=0.0,
        balance=1000.0
    ),
    # BankStatement(
    #     id='ac7baff0-8f2f-48c8-8921-115e5cb8e26a',
    #     document='123456789011',
    #     agency=3245,
    #     account_number=38913,
    #     account_digit=3,
    #     type='checking_account',
    #     date='2023-06-06 00:00:00',
    #     description="Transferência para conta corrente",
    #     transaction_value=100.0,
    #     balance=500.0
    # ),
    BankStatement(
        id='0ee801ab-6249-4e19-82d6-e180ef0d0a34',
        document='123456789011',
        agency=3312,
        account_number=98109,
        account_digit=5,
        type='savings_account',
        date='2023-06-06 21:00:00',
        description="Transferência para poupança",
        transaction_value=0.0,
        balance=1.0
    ),
    # BankStatement(
    #     id='0ee801ab-6249-4e19-82d6-e180ef0d0a34',
    #     document='123456789011',
    #     agency=1233,
    #     account_number=90102,
    #     account_digit=2,
    #     type='checking_account',
    #     date='2023-06-06 10:30:00',
    #     description="Transferência para conta corrente",
    #     transaction_value=100.0,
    #     balance=70.0
    # ),
]
