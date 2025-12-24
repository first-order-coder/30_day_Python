class BankError(Exception): #this is a custom exception error
    "Base class for all bank domain errors"

class InvalidAmountError(BankError):
    pass

class InsufficietFundsError(BankError):
    pass

class AccountNotFoundError(BankError):
    pass

class CustomerNotFoundError(BankError):
    pass

class AccountClosedError(BankError):
    pass

class SameAccontTransferError(BankError):
    pass
