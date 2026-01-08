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

@dataclass(frozen=True) #no values are assigned or cannot be assigned directly
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
        self._transactions: list[Transaction] = [] #this is a list of Transaction classes
        
    @property
    def balance(self) -> float:
        return self._balance # to read this balance we can use balance instead of _balance

    @property
    def is_closed(self) -> bool:
        return self._closed
    
    def close(self):
        self._closed = True

    def _ensure_open(self):
        if self._closed:
            raise AccountClosedError(f"Account {self.account_id} is closed.")
    
    @staticmethod
    def _validate_amount(amount: float):
        if amount <= 0:
            raise InvalidAmountError("Amount must be > 0.")
        
    def deposit(self, amount: float, note:str = ""):
        self._ensure_open()
        self._validate_amount(amount)

        self._balance += amount
        self._transactions.append(
            Transaction(
                tx_type="deposit",
                amount=amount,
                timestamp=datetime.now(datetime.utc),
                note=note,
                to_account=self.account_id,
            )
        )
    
    def withdraw(self, amount: float, note:str = ""):
        self._ensure_open()
        self._validate_amount(amount)

        self._withdraw_rule_check(amount)

        self._balance -= amount
        self._transactions.append(
            Transaction(
                tx_type="withdraw",
                amount=amount,
                timestamp=datetime.now(datetime.utc),
                note=note,
                to_account=self.account_id,
            )
        )
    
    @abstractmethod
    def _withdraw_rule_check(self, amount:float):
        """Eac accoun type impelemnts withdrawal rule checks."""
    
    def transactions(self):
        return list(self._transactions)


