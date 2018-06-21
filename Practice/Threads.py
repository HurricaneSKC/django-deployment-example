import threading
import time
import random

# setting a sub-class of threading.py
class BankAccount(threading.Thread):

    # set account balance
    acctBalance = 100

    # initialise class - customer name & amount of money requested
    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)

        self.name = name
        self.moneyRequest = moneyRequest

    #
    def run(self):
        threadLock.acquire()

        BankAccount.getMoney(self)

        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name,
                                                        customer.moneyRequest,
                                                        time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance : ${}".format(BankAccount.acctBalance))
        else:
            print("Not enough money in account")
            print("Current balance : ${}".format(BankAccount.acctBalance))

        time.sleep(3)

threadLock = threading.Lock()

doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 50)

doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()