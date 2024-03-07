class BankAccount:
    """
    A class to represent a bank account.
    ...

    Attributes
    ----------
    balance : int
        balance of the bank account
    account_number : int
        bank account number

    Methods
    -------
    topup(amount: int):
        Topups account's balance.
    withdraw(amount: int):
        Withdraws an amount from account's balance.
    """

    # class attribute to keep track of accounts amount
    accounts_counter = 0

    def __init__(self, balance: int = 0) -> None:
        """
        Constructs all the necessary attributes for the bank account object.
        :param balance:
        """

        # increasing accounts counter each time instance created
        BankAccount.accounts_counter += 1
        self.balance = balance
        # using accounts counter to set a unique account number for each instance
        self.account_number = BankAccount.accounts_counter

    def __str__(self) -> str:
        """
        String representation of account's information.
        :return:
        """
        return (f"Your account number: {self.account_number}\n"
                f"Your balance is: {self.balance} USD.")

    def topup(self, amount: int) -> int:
        """
        Topups account's balance.
        :param amount:
        :return:
        """
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int) -> int:
        """
        Withdraws an amount from account's balance.
        :param amount:
        :return:
        """
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        print("You have insufficient balance!")
