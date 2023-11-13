from brownie import fundMe
from scripts.helpful import get_account
import time


def fund():
    account = get_account()
    _fundMe = fundMe[-1]
    entrance_fee = _fundMe.getEntranceFee()
    print("The entrance fee is: ", entrance_fee)
    print(f"Current ethh_USD price is :{_fundMe.getPrice()}")
    tx = _fundMe.fundme({"from": account, "value": entrance_fee})
    tx.wait(1)
    time.sleep(1)


def withdraw():
    account = get_account()
    _fundMe = fundMe[-1]
    tx = _fundMe.withdraw({"from": account})
    tx.wait(1)
    time.sleep(1)


def main():
    fund()
    withdraw()
