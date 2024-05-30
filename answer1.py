import requests

def get_block_hash(block):
    try:
        url = f"https://api.blockcypher.com/v1/btc/test3/blocks/{block}"
        response = requests.get(url)
        response.raise_for_status()
        block_hash = response.json()["hash"]
        return block_hash
    except Exception as error:
        print("Error fetching block data:", error)
        raise

block = 2817677

try:
    hash_value = get_block_hash(block)
    print(f"Hash for block {block}: {hash_value}")
except Exception as error:
    print("Error:", error)
