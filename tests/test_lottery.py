from brownie import accounts, config, network
from web3 import Web3
from scripts.helpful_scripts import deploy_lottery


def test_get_enterance_fee():
    lottery = deploy_lottery()
    assert lottery.getEntranceFee() > Web3.toWei(0.016, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.020, "ether")
