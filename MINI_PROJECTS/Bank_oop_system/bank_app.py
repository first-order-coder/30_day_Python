from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from abc import ABC, abstractmethod

class BankError(Exception):
    "This is the base class which inherits from Exception parent class"

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountNotFoundError(BankError):
    pass

class CustomerNotFoundError(BankError):
    pass

class AccountClosedError(BankError):
    pass

class SameAccountTransferError(BankError):
    pass

@dataclass(frozen=True)
class Transaction:
    tx_type: str
    amount: float
    timestamp: datetime
    note: str = ""
    from_account = None
    to_account = None

class Account(ABC):
    def __init__(self, account_id: str, owner_id: str) -> None: #ids are identifiers, therefore kept as strings
        self.account_id = account_id
        self.owner_id = owner_id
        self._balance = 0.0 #starts from default value, anyone calling this class cannot change them
        self._closed = False
        self._transactions: list[Transaction] = []

    @property
    def balance(self) -> float:
        return self._balance # to read this balance we can use balance instead of _balance