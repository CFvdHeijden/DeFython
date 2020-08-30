from web3 import Web3

#DEX addresses
kyberNetworkProxy = "0x818E6FECD516Ecc3849DAf6845e3EC868087B755"

#Uniswap factory address
UniswapV2Factory = "0xc0a47dFe034B400B47bDaD5FecDa2621de6c4d95"

#Token Addresses on kyber
kyberDai = Web3.toChecksumAddress("0x6b175474e89094c44da98b954eedeac495271d0f")
kyberUsdc = Web3.toChecksumAddress("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
kyberWeth = Web3.toChecksumAddress("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")

#Token Addresses on Uniswap
uniswapEth = "0x0000000000000000000000000000000000000000"
uniswapBat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
uniswapDai = "0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359"