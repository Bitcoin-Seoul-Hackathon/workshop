import requests

async def get_txcount(block):
    try:
        url = f"https://api.blockcypher.com/v1/btc/test3/blocks/{block}"
        response = requests.get(url)
        response.raise_for_status()
        txcount = response.json()["n_tx"]
        return txcount
    except Exception as error:
        print("Error fetching block data:", error)
        raise

async def main():
    block = 2817678

    try:
        count = await get_txcount(block)
        print(f"Number of new outputs created by block at block {block}: {count}")
    except Exception as error:
        print("Error from fetching outputs:", error)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
