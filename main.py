"""The main class for the project """
import datetime
import uuid


class BankAccount:
    """Accounts base class."""

    def __init__(self, acc_holder_name, initial_balance=0):

        # Generate unique account number
        self.account_number = str(uuid.uuid4())[:8]
        self.acc_holder_name = acc_holder_name
        self._balance = initial_balance  # private attribute
        self.creation_date = datetime.datetime.now()
        self.transaction_history = []

        if initial_balance > 0:
            # Recording the initial balance
            self._add_transaction("Initial deposit", initial_balance)

    def deposit(self, amount):
        """Deposit method."""
        if amount < 0:
            raise ValueError("Deposit amount must be positive!!.")

        self._balance += amount
        self._add_transaction("Deposit", amount)
        return f"Deposited R{amount:.2f}.\nNew balance: R{self._balance:.2f}"

    def withdraw(self, amount):
        """Withdraw amount"""
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be below 0")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
        self._add_transaction("Withdrawal:", -amount)
        return f"Withdrew R{amount:.2f}.\nNew balance is R{self._balance:.2f}"

    def get_balance(self):
        """Get Current balance"""
        now = datetime.datetime.now()
        return f"Balance as as {now.strftime('%Y-%m-%d %H:%M:%S')}: R{self._balance}"

    def display_info(self):
        """Display the account holder's information."""
        return (
            f"Account Number: {self.account_number} \
            \nAccount holder: {self.acc_holder_name} \
            \nBalance: R{self._balance} \
            \nCreated on: {self.creation_date.strftime('%Y-%m-%d')}"
        )

    def view_transactions(self):
        """View the transaction history of the particular account."""
        if not self.transaction_history:
            return "No transactions found."

        history = "Transaction history:\n"
        for idx, transaction in enumerate(self.transaction_history, 1):
            amount = transaction["amount"]
            sign = "+" if amount >= 0 else ""
            history += f"{idx}. {transaction['timestamp'].strftime('%Y-%m-%d %H:%M')} \
                {transaction['type']}: {sign}R{abs(amount):.2f}\n"

        return history

    def _add_transaction(self, transaction_type, amount):
        """Add transaction to history."""
        timestamp = datetime.datetime.now()
        self.transaction_history.append({
            "timestamp": timestamp,
            "type": transaction_type,
            "amount": amount,
            "balance": self._balance
        })


def main():
    kupa = BankAccount("Nicholas Chamboko", 5000)
    print(kupa.deposit(150))
    print(kupa.withdraw(2050))
    print(kupa.get_balance())
    print(kupa.display_info())
    print(kupa.view_transactions())


if __name__ == "__main__":
    main()
