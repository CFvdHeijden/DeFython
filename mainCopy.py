from web3 import Web3
import asyncio
import json
import abi

#auto detects local running node:
#from web3.auto import w3

#Manually connect to local geth node
my_provider = Web3.IPCProvider('/home/no/.ethereum/geth.ipc')
w3 = Web3(my_provider)


def handle_event(event):
    print(w3.eth.blockNumber)

async def log_loop(event_filter):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)

def main():
    block_filter = w3.eth.filter('latest')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(block_filter)))
    finally:
        loop.close()

if __name__ == '__main__':
    main()