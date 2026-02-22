"""Bank Account — complete OOP exercise.

Exercises:
  1. Create BankAccount with owner, balance, and transaction history
  2. Implement deposit() and withdraw() with validation
  3. Implement transfer() between accounts
  4. Track transaction history and implement __str__
"""


class BankAccount:
    """A bank account with transaction history."""

    def __init__(self, owner, balance=0):
        # TODO: Initialize owner, balance, and empty transaction list
        pass

    def deposit(self, amount):
        """Deposit money. Amount must be positive."""
        # TODO: Validate amount > 0, update balance, record transaction
        pass

    def withdraw(self, amount):
        """Withdraw money. Must have sufficient funds."""
        # TODO: Validate amount > 0 and sufficient balance
        # TODO: Update balance, record transaction
        pass

    def transfer(self, other, amount):
        """Transfer money to another account."""
        # TODO: Withdraw from self, deposit to other
        pass

    def get_history(self):
        """Return transaction history."""
        # TODO: Return the list of transactions
        pass

    def __str__(self):
        # TODO: Return "owner: $balance"
        pass


def main():
    # TODO: Create accounts, perform operations, show history
    # Hint: alice = BankAccount("Alice", 1000)
    # Hint: bob = BankAccount("Bob", 500)
    # Hint: alice.deposit(200)
    # Hint: alice.transfer(bob, 300)
    pass  # Remove when done


if __name__ == "__main__":
    main()
