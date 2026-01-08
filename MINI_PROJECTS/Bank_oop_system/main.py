from domain import BankError
from bank_service import Bank


def main() -> None:
    bank = Bank()
    try:
        alice = bank.create_customer("Alice")
        checking = bank.open_checking(alice.customer_id, overdraft_limit=100.0)
        savings = bank.open_savings(alice.customer_id)

        checking.deposit(500.0, "Initial deposit")
        bank.transfer(checking.account_id, savings.account_id, 200.0, "Move to savings")
        checking.withdraw(350.0, "Rent")  # 500 - 200 - 350 = -50 (allowed)

        print("Customer:", alice.customer_id, alice.name)
        print("Checking:", checking.account_id, "balance =", checking.balance)
        print("Savings: ", savings.account_id, "balance =", savings.balance)

        print("\nChecking transactions:")
        for tx in checking.transactions():
            print(f"  {tx.timestamp.isoformat()} {tx.tx_type} {tx.amount} note={tx.note}")

        print("\nSavings transactions:")
        for tx in savings.transactions():
            print(f"  {tx.timestamp.isoformat()} {tx.tx_type} {tx.amount} note={tx.note}")

    except BankError as e:
        print("Bank error:", e)


if __name__ == "__main__":
    main()
