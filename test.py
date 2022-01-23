import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()
infura_key = os.environ.get("INFURA_ENDPOINT")

exponent = 10 **18

w3 = Web3(Web3.HTTPProvider(infura_key))

lp_address = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"
checksummed_contract = w3.toChecksumAddress(lp_address)

with open("abis/aave.json") as f:
    abi_aave = json.load(f)

contract = w3.eth.contract(address = checksummed_contract, abi = abi_aave)
data = contract.functions.decimals.call()

print(data)
