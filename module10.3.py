import threading


class BankAccount():
    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self, amount1):
        with self.lock:
            self.amount1 = amount1
            self.balance += self.amount1
            print(f'Deposited {self.amount1}, new balance is {self.balance}')

    def withdraw(self, amount2):
        with self.lock:
            self.amount2 = amount2
            self.balance -= self.amount2
            print(f'Withdraw {self.amount2}, new balance is {self.balance}')


def deposit_task(account, amout):
    for _ in range(5):
        account.deposit(amout)


def withdraw_task(account, amout):
    for _ in range(5):
        account.withdraw(amout)

lock = threading.Lock()
account = BankAccount(1000, lock=lock)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))


deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

