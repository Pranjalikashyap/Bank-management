import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"

    def __init__(self):
        self.info = self.load_data()

    def load_data(self):
        if Path(self.database).exists():
            with open(self.database, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.database, "w") as f:
            json.dump(self.info, f, indent=4)

    def generate_account(self):
        chars = random.choices(string.ascii_uppercase, k=3)
        nums = random.choices(string.digits, k=4)
        return ''.join(chars + nums)

    def create_account(self, name, age, email, pin):
        if age < 18:
            return "Age must be 18+"

        if len(str(pin)) != 4:
            return "PIN must be 4 digits"

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.generate_account(),
            "balance": 0
        }

        self.info.append(account)
        self.save_data()
        return account

    def login(self, accountNo, pin):
        for user in self.info:
            if user["accountNo"] == accountNo and user["pin"] == pin:
                return user
        return None

    def deposit(self, accountNo, pin, amount):
        user = self.login(accountNo, pin)
        if not user:
            return "Invalid account"

        user["balance"] += amount
        self.save_data()
        return "Deposit successful"

    def withdraw(self, accountNo, pin, amount):
        user = self.login(accountNo, pin)

        if not user:
            return "Invalid account"

        if user["balance"] < amount:
            return "Insufficient balance"

        user["balance"] -= amount
        self.save_data()
        return "Withdrawal successful"

    def delete_account(self, accountNo, pin):
        user = self.login(accountNo, pin)

        if not user:
            return "Invalid account"

        self.info.remove(user)
        self.save_data()
        return "Account deleted"