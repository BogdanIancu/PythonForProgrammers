from threading import Thread, Lock
import time
import random


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            print("Deposit started")
            current_balance = self.balance
            current_balance += amount
            # Simulating some processing time
            time.sleep(random.randint(1, 3))
            self.balance = current_balance
            print(f"Deposit completed. Balance: {self.balance}")

    def withdraw(self, amount):
        self.lock.acquire()
        print("Withdrawal started")
        current_balance = self.balance
        if current_balance >= amount:
            current_balance -= amount
            # Simulating some processing time
            time.sleep(random.randint(1, 3))
            self.balance = current_balance
            print(f"Withdrawal completed. Balance: {self.balance}")
        else:
            print("Insufficient funds")
        self.lock.release()


bank_account = BankAccount(balance=500)

wife_thread = Thread(target=bank_account.withdraw, args=(200,))
husband_thread = Thread(target=bank_account.deposit, args=(300,))

wife_thread.start()
husband_thread.start()

wife_thread.join()
husband_thread.join()

print(f"Final balance: {bank_account.balance}")
