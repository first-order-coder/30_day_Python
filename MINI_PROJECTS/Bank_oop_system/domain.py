from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Optional


# =========================
# Exceptions
# =========================

class BankError(Exception):
    """Base class for all bank domain errors."""


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class AccountClosedError(BankError):
    pass


class SameAccountTransferError(BankError):
    pass


class AccountNotFoundError(BankError):
    pass


class CustomerNotFoundError(BankError):
    pass


# =========================
# Transaction (audit record)
# =========================

@dataclass(frozen=True)
class Transaction:
    tx_type: str                 # "deposit" | "withdraw"
    amount: float
    timestamp: datetime
    note: str = ""
    from_account: Optional[str] = None
    to_account: Optional[str] = None


# =========================
# Account (base) + types
# =========================

class Account(ABC):
    def __init__(self, account_id: str, owner_id: str) -> None:
        self.account_id = account_id
        self.owner_id = owner_id
        self._balance: float = 0.0
        self._closed: bool = False
        self._transactions: list[Transaction] = []

    @property
    def balance(self) -> float:
        """Read-only access to balance."""
        return self._balance

    @property
    def is_closed(self) -> bool:
        return self._closed

    def close(self) -> None:
        self._closed = True

    def _ensure_open(self) -> None:
        if self._closed:
            raise AccountClosedError(f"Account {self.account_id} is closed.")

    @staticmethod
    def _validate_amount(amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("Amount must be > 0.")

    def deposit(self, amount: float, note: str = "") -> None:
        self._ensure_open()
        self._validate_amount(amount)

        self._balance += amount
        self._transactions.append(
            Transaction(
                tx_type="deposit",
                amount=amount,
                timestamp=datetime.utcnow(),
                note=note,
                to_account=self.account_id,   # MUST match dataclass field name
            )
        )

    def withdraw(self, amount: float, note: str = "") -> None:
        self._ensure_open()
        self._validate_amount(amount)

        self._withdraw_rule_check(amount)

        self._balance -= amount
        self._transactions.append(
            Transaction(
                tx_type="withdraw",
                amount=amount,
                timestamp=datetime.utcnow(),
                note=note,
                from_account=self.account_id,  # MUST match dataclass field name
            )
        )

    @abstractmethod
    def _withdraw_rule_check(self, amount: float) -> None:
        """Subclasses enforce withdrawal rules."""

    def transactions(self) -> list[Transaction]:
        return list(self._transactions)


class SavingsAccount(Account):
    def _withdraw_rule_check(self, amount: float) -> None:
        if self._balance < amount:
            raise InsufficientFundsError("Savings cannot be overdrawn.")


class CheckingAccount(Account):
    def __init__(self, account_id: str, owner_id: str, overdraft_limit: float = 0.0) -> None:
        super().__init__(account_id, owner_id)
        if overdraft_limit < 0:
            raise InvalidAmountError("Overdraft limit must be >= 0.")
        self.overdraft_limit = overdraft_limit

    def _withdraw_rule_check(self, amount: float) -> None:
        if (self._balance - amount) < -self.overdraft_limit:
            raise InsufficientFundsError("Overdraft limit exceeded.")


# =========================
# Customer
# =========================

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.account_ids: list[str] = []
