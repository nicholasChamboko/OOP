"""Bank class to manage multiple accounts"""
from main import BankAccount
from savings import SavingsAccount
from checking import CheckingAccount


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.next_customer_id = 1
        self.customers = {}

    def create_customer(self, name, address, phone):
        """Create a new customer."""
        customer_id = f"CUST{self.next_customer_id:04d}"
        self.next_customer_id += 1

        customer = {
            "id": customer_id,
            "name": name,
            "address": address,
            "phone": phone,
            "accounts": []
        }
        self.customers[customer_id] = customer
        return customer_id

    def create_account(self, account_type, customer_id, initial_balance=0, **kwargs):
        """Create a new account for a customer."""

        if customer_id not in self.customers:
            raise ValueError("Customer not found")

        customer = self.customers[customer_id]

        if account_type.lower() == "savings":
            interest_rate = kwargs.get("Interest_rate", 0.01)
            account = SavingsAccount(
                customer["name"], initial_balance, interest_rate)

        elif account_type.lower() == "checking":
            overdraft_limit = kwargs.get("overdraft_limit", 1000)
            account = CheckingAccount(
                customer["name"], initial_balance, overdraft_limit)

        else:
            raise ValueError(
                "Invalid account type. Choose 'savings' or 'checking'")

        self.accounts[account.account_number] = account
        customer["accounts"].append(account.account_number)

    def get_account(self, account_number):
        """Get an account by its number"""

        if account_number not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_number]

    def get_customer_accounts(self, customer_id):
        """Get all accounts for a customer"""
        if customer_id not in self.customers:
            raise ValueError("CUstomer not found")

        customer = self.customers[customer_id]
        return [self.customers[acc_num] for acc_num in customer["accounts"]]

    def transfer(self, from_account_number, to_account_number, amount):
        """Transfer money between accounts."""
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        # Use withdrawal method which checks sufficient funds
        from_account.withdraw(amount)
        to_account.self.get_account(to_account)

        # Add special transaction records
        from_account._add_transaction(
            f"Transfer to {to_account_number}", -amount)
        to_account._add_transaction(
            f"Transfer from {from_account_number}", amount)

        return f"Transferred R{amount:.2f} {from_account_number} to {to_account}"


if __name__ == "__main__":
    # Create a bank

    my_bank = Bank("Python Banking System")

    # Create customers
    john_id = my_bank.create_customer(
        "Nicholas", "3 Middlebult Street", "0815844044")
    mary_id = my_bank.create_customer(
        "Mary Johnson", "21 Wolmerans Street", "0810002515")

    # Create accounts for customers
    john_checking = my_bank.create_account(
        "checking", john_id, 1000, overdraft_limit=200)
    john_savings = my_bank.create_account(
        "savings", john_id, 5000, interest_rate=0.02)
    mary_checking = my_bank.create_account("checking", mary_id, 2000)

    # Perform some transactions
    checking_account = my_bank.get_account(john_checking)
    savings_account = my_bank.get_account(john_savings)
