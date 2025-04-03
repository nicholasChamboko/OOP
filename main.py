import datetime
import uuid


class BankAccount:
    """Accounts base class."""

    def __init__(self, acc_holder_name, initial_balance=0):

        # Generate unique account number
        self.account_number = str(uuid.uuid4())[:8]
        self.acc_holder_name = acc_holder_name
        self.balance = initial_balance
        self.creation_date = datetime.datetime.now()
        self.transaction_history = []
