class BankError(Exception):
    "base class for all exceptions"

class AccountNotFoundError(BankError):
    def __init__(self, account_id):
        super().__init__(f"Account not found: {account_id}") #when account id is not in the account dict
        self.account_id = account_id

class InsufficientFundsError(BankError):
    def __init__(self, balance, amount) -> None:
        super().__init__(f"Insufficient funds: balance={balance}, requested={amount}")
        self.balance = balance
        self.amount = amount

class NegativeAmountError(BankError):
    def __init__(self, amount) -> None:
        super().__init__(f"Amount must be positive. Got: {amount}") #raised when someone tries to deposit/withdraw 0 or negative 
        self.amount = amount

def get_account(accounts, account_id):
    if account_id not in accounts:
        raise AccountNotFoundError(account_id) #if the account Id doesnt exist it will return an error
    return accounts[account_id] #returns the balance if account doesn't exist -> accounts = {"account_id": balance}

def deposit(accounts, account_id, amount): 
    if amount <= 0:
        raise NegativeAmountError(amount)
    accounts[account_id] = get_account(accounts, account_id) + amount #adding balance + amount 

def withdraw(accounts, account_id, amount):
    if amount <= 0:
        raise NegativeAmountError(amount)
    balance = get_account(accounts, account_id) #must decalare a instance of the function to use the returned value
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    accounts[account_id] = balance - amount #else the accounts dict will update with new balance after amount has been taken off

accounts = {"A1": 100}

actions = [("deposit", "A1", 500), ("withdraw", "A1", 200), ("deposit", "A1", -5), ("withdraw", "X9", 10), ("withdraw", "A1", 50)]
for action in actions:
    try:
        op, id, amt = action
        if op == "deposit":
            deposit(accounts, id, amt)
            print("deposited",amt, "Balance", accounts[id])
        else:
            withdraw(accounts, id, amt)
            print(amt)
    except BankError as e:
        print("BankError:", e) 
    