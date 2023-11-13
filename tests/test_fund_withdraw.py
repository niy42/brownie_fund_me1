from scripts.helpful import get_account, LBEnvs
from scripts.deploy import deploy_fundMe
import time, pytest
from brownie import accounts, network, exceptions


def test_can_fund_withdraw():
    account = get_account()
    _fundMe = deploy_fundMe()
    entrance_fee = _fundMe.getEntranceFee()
    tx = _fundMe.fundme({"from": account, "value": entrance_fee})
    tx.wait(1)
    time.sleep(1)
    assert _fundMe.addresstoamountFunded(account.address) == entrance_fee
    tx = _fundMe.withdraw({"from": account})
    tx.wait(1)
    time.sleep(1)
    assert _fundMe.addresstoamountFunded(account.address) == 0


def test_onlyOwner():
    if network.show_active() not in LBEnvs:
        pytest.skip("Only for local testing...")
    _fundMe = deploy_fundMe()
    account = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        _fundMe.withdraw({"from": account})
