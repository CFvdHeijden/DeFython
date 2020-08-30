from web3 import Web3
import asyncio
import json
import abi
import addresses

#auto detects local running node:
#from web3.auto import w3

#Manually connect to local geth node
my_provider = Web3.IPCProvider('/home/no/.ethereum/geth.ipc')
w3 = Web3(my_provider)

#Create kyber object to communicate with kyber smart contract
kyber = w3.eth.contract(abi = abi.kyberABI, address = addresses.kyberNetworkProxy)
#Create uniswap object to communicate with uniswap smart contract
#uniswap = w3.eth.contract(abi = abi.uniswapABI, address = addresses.UniswapV2Factory)

#------------------------------------------------------------------------------------#
# ---------->  THIS SHOULD BE CHANGED TO API CALL FOR ACTUAL PRICES  <---------------#
AMOUNT_ETH = 100
RECENT_ETH_PRICE = 400
#------------------------------------------------------------------------------------#

#Format the numbers
AMOUNT_ETH_inWEI = Web3.toWei(AMOUNT_ETH, 'ether')
FOR_AMOUNT_DAI_inWEI = AMOUNT_ETH * RECENT_ETH_PRICE
AMOUNT_DAI_inWEI = Web3.toWei(FOR_AMOUNT_DAI_inWEI, 'ether')

def handle_event(event):
    #Do things for new block starting with printing latest block number
    print(w3.eth.blockNumber)



    #uniswapResults = [
    #    uniswap.getExchange(
    #        addresses.uniswapDai
    #        #addresses.uniswapEth
    #        )
    #]
    #print(uniswapResults)

    #Call kyber smart contract for price
    kyberResults = [
        kyber.caller().getExpectedRate(
            addresses.kyberDai,
            Web3.toChecksumAddress('0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'),
            10000000000
            #AMOUNT_DAI_inWEI
        ),
        kyber.caller().getExpectedRate(
            Web3.toChecksumAddress('0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'),
            addresses.kyberDai,
            10000
            #AMOUNT_ETH_inWEI
        )]
    print(kyberResults)

    #Do some magic on numbers for readability
    kyberRates = {
        "buy" : float(1 / (kyberResults[0][0] / (10**18))),
        "sell" : float(kyberResults[1][0] / (10**18))
    }
    print("Kyber ETH/DAI prices")
    print(kyberRates)

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