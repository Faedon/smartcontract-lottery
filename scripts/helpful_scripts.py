from brownie import network, Lottery, accounts, config


def deploy_lottery():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )


def main():
    deploy_lottery()
