"""SavingsAccount inherits from the Bank Class."""

import datetime
from main import BankAccount


class SavingsAccount(BankAccount):
    """Savings account with interest rates."""

    def __init__(self, acc_holder_name, initial_balance=0, interest_rate=0.01):

        # Calling parent class constructor
        super().__init__(acc_holder_name, initial_balance)
        self.account_type = "Savings"
        self.interest_rate = interest_rate
        self.last_interest_date = self.creation_date

    def add_interest(self):
        """Adding interest to the account based on the current balance."""
        interest_amount = self._balance * self.interest_rate
        self._balance += interest_amount
        self._add_transaction("Interest", interest_amount)
        self.last_interest_date = datetime.datetime.now()
        return f"Added interest: R{interest_amount:.2f}. New balance: R{self._balance:.2f}"

    def display_info(self):
        """Overriding the display_info method to include interest rate"""
        basic_info = super().display_info()
        return (
            f"{basic_info}\nAccount Type: {self.account_type} \
                \nInterest Rate: {self.interest_rate:.2f}"
        )


def main():
    pass


if __name__ == "__main__":
    main()
