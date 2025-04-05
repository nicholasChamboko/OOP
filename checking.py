""" Checking account child class"""
from main import BankAccount


class CheckingAccount(BankAccount):
    """Checking account has an overdraft feature"""

    def __init__(self, acc_holder_name, initial_balance=0, overdraft_limit=100):
        super().__init__(acc_holder_name, initial_balance)
        self.account_type = "Checking"
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Overriding the main withdraw method to accommodate overdraft"""
        if amount <= 0:
            raise ValueError(f"Withdrawal of {amount} cannot be below 0.")

        if amount > (self._balance + self.overdraft_limit):
            raise ValueError(
                (
                    f"The amount exceeds the overdraft limit. \
                    Max withdrawal: R{self._balance + self.overdraft_limit:.2f}")
            )

        self._balance -= amount
        self._add_transaction("Withdrawal", -amount)

        if self._balance < 0:
            return f"Withdrew R{amount:.2f} (Overdraft: R{abs(self._balance):.2f})"
        else:
            return f"Withdrew R{amount:.2f}. New ballance: R{self._balance:.2f}"

    def display_info(self):
        """Override to include overdraft information"""
        basic_info = super().display_info()
        return (
            f"{basic_info}\n"
            f"Account Type: {self.account_type}\n"
            f"Overdraft Limit: R{self.overdraft_limit:.2f}"
        )


def main():
    pass


if __name__ == "__main__":
    main()
