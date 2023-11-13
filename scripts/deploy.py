# Project Title - deploy.py (fundMe)
# Project completed by niy42

# importing neccessary packages
from brownie import fundMe, MockV3Aggregator, network, config
from scripts.helpful import get_account, deploy_mocks, LBEnvs
from brownie.network.gas.strategies import ExponentialScalingStrategy
from brownie.network.gas.strategies import LinearScalingStrategy

# gas strategies dynamically generates a gas price for a transaction
# there are two types based on time scaling strategy
# your choice of gas strategy might depend on waiting time
gas_strategy = ExponentialScalingStrategy("10 gwei", "50 gwei")
gas_strategy1 = LinearScalingStrategy("10 gwei", "50 gwei", 1.1)


# deploys fundMe contract
def deploy_fundMe():
    account = get_account()
    if network.show_active() not in LBEnvs:
        priceFeed = config["networks"][network.show_active()]["eth_usd_price"]
    else:
        deploy_mocks()
        priceFeed = MockV3Aggregator[-1].address
    _fundMe = fundMe.deploy(
        priceFeed,
        {"from": account, "gasPrice": gas_strategy},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print("The current eth/USD price is: ", _fundMe.getPrice())
    print(f"Fundme deployed at {_fundMe.address}")
    return _fundMe


# main calls deploy_fundMe function
def main():
    deploy_fundMe()


# Note - brownie works with compiled JSON files.
