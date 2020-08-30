from web3 import Web3
import web3
import asyncio
import json
import abi
import addresses
import secrets

from dydx.client import Client
import dydx.constants as consts
import dydx.util as utils

#Connect with my node
my_provider = Web3.IPCProvider('/home/no/.ethereum/geth.ipc')
w3 = Web3(my_provider)
connect = w3.isConnected()
print(connect)

# create a new client with a private key (string or bytearray)
client = Client(
    private_key= secrets.key,
    node='https://mainnet.infura.io/v3/a9ff793dc5c949c783aabd3da87c96aa'
)

# Get all trading pairs for dydx
#pairs = client.get_pairs()
#print(pairs)

# Get index price
index_prices = client.get_funding_index_price()
print(index_prices)

# Get Individual Index price
index_price = client.get_funding_index_price(markets=['WETH-USDC'])
print(index_price)