from __future__ import annotations

from domain import (
    Customer,
    Account,
    SavingsAccount,
    CheckingAccount,
    AccountNotFoundError,
    CustomerNotFoundError,
    SameAccountTransferError,
)


class Bank:
    def __init__(self) -> None:
        self._customers: dict[str, Customer] = {}
        self._accounts: dict[str, Account] = {}
        self._next_customer_num = 1
        self._next_account_num = 1

    def _new_customer_id(self) -> str:
        cid = f"C{self._next_customer_num:06d}"
        self._next_customer_num += 1
        return cid

    def _new_account_id(self) -> str:
        aid = f"A{self._next_account_num:06d}"
        self._next_account_num += 1
        return aid

    # Customers
    def create_customer(self, name: str) -> Customer:
        cid = self._new_customer_id()
        c = Customer(cid, name)
        self._customers[cid] = c
        return c

    def get_customer(self, customer_id: str) -> Customer:
        c = self._customers.get(customer_id)
        if not c:
            raise CustomerNotFoundError(f"Customer not found: {customer_id}")
        return c

    # Accounts
    def open_savings(self, customer_id: str) -> SavingsAccount:
        c = self.get_customer(customer_id)
        aid = self._new_account_id()
        acc = SavingsAccount(aid, c.customer_id)
        self._accounts[aid] = acc
        c.account_ids.append(aid)
        return acc

    def open_checking(self, customer_id: str, overdraft_limit: float = 0.0) -> CheckingAccount:
        c = self.get_customer(customer_id)
        aid = self._new_account_id()
        acc = CheckingAccount(aid, c.customer_id, overdraft_limit=overdraft_limit)
        self._accounts[aid] = acc
        c.account_ids.append(aid)
        return acc

    def get_account(self, account_id: str) -> Account:
        acc = self._accounts.get(account_id)
        if not acc:
            raise AccountNotFoundError(f"Account not found: {account_id}")
        return acc

    # Transfer
    def transfer(self, from_id: str, to_id: str, amount: float, note: str = "") -> None:
        if from_id == to_id:
            raise SameAccountTransferError("Cannot transfer to the same account.")

        from_acc = self.get_account(from_id)
        to_acc = self.get_account(to_id)

        from_acc.withdraw(amount, note=f"Transfer to {to_id}. {note}".strip())
        to_acc.deposit(amount, note=f"Transfer from {from_id}. {note}".strip())
