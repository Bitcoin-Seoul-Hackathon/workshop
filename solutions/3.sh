#!/bin/bash

block_number=$((2817692 + 1))
endpoint="https://bitcoin-testnet.g.allthatnode.com/archive/json_rpc"

printf \
"
   ____                  _   _               ____  
  / __ \                | | (_)             |___ \ 
 | |  | |_   _  ___  ___| |_ _  ___  _ __     __) |
 | |  | | | | |/ _ \/ __| __| |/ _ \| '_ \   |__ < 
 | |__| | |_| |  __/\__ \ |_| | (_) | | | |  ___) |
  \___\_\\\\\\\\__,_|\___||___/\__|_|\___/|_| |_| |____/ 
                                                   
                                                   

How many new outputs were created by block $block_number?

=========================================

"

# Get the block hash from block height
output=$(curl -s $endpoint \
--request POST \
--header "Content-Type: text/plain" \
--data "{ 
  \"jsonrpc\": \"1.0\", 
  \"id\": \"0\", 
  \"method\": \"getblockhash\", 
  \"params\": [$block_number] 
}")

block_hash=$(echo $output | jq -r '.result')
error=$(echo $output | jq -r '.error')

if [ "$error" != "null" ]
then
  echo "Something went wrong on the getblockhash call: $error"
  exit 1
fi

printf "Block Hash: $block_hash\n"

# Get block details, especially tx list
output=$(curl -s $endpoint \
--request POST \
--header "Content-Type: text/plain" \
--data "{ 
  \"jsonrpc\": \"1.0\", 
  \"id\": \"0\", 
  \"method\": \"getblock\", 
  \"params\": [\"$block_hash\"] 
}")

txs=$(echo $output | jq -r '.result.tx')
tx_count=$(echo $output | jq -r '.result.tx | length')
error=$(echo $output | jq -r '.error')

if [ "$error" != "null" ]
then
  echo "Something went wrong on the getblock call: $error"
  exit 1
fi

printf "Length of txs: $tx_count\n"

txs_trimmed=$(echo $txs | jq -r '.[]' | sed 's/.*/"&"/' | tr '\n' ' ')
IFS=' ' read -r -a tx_array <<< "$txs_trimmed"

count=0
vout_counts=0

for tx in "${tx_array[@]}"
do
  count=$((count + 1))

  output=$(curl -s $endpoint \
  --request POST \
  --header "Content-Type: application/json" \
  --data "{ 
    \"jsonrpc\": \"1.0\", 
    \"id\": \"0\", 
    \"method\": \"getrawtransaction\", 
    \"params\": [$tx, true] 
  }")
  
  result=$(echo $output | jq -r '.result')
  error=$(echo $output | jq -r '.error')

  if [ "$error" != "null" ]
  then
    printf "At transaction $count\n"
    printf "Something went wrong on the getrawtransaction call: $error\n"
    exit 1
  fi
  
  # # Extract the number of outputs (vout length)
  vout_count=$(echo $result | jq '.vout | length')
  vout_counts=$((vout_counts + vout_count))  

  if [ $((count % 10)) -eq 0 ]
  then
    printf "Current vout counts: $vout_counts, count: $count\n"

    # Sleep for 1 second to avoid rate limit
    sleep 1
  fi
done

printf "Total vout counts: $vout_counts\n"
