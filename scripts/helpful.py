from brownie import accounts, network, config, MockV3Aggregator

DECIMALS = 8
STARTING_PRICE = 300000000000
LBEnvs = ["development", "ganache-local"]
FORKED_Envs = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if network.show_active() in LBEnvs or FORKED_Envs:
        return accounts[3]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
