#!/bin/bash

address="1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
message="1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
signature="HCsBcgB+Wcm8kOGMH8IpNeg0H4gjCrlqwDf/GlSXphZGBYxm0QkKEPhh9DTJRp2IDNUhVr0FhP9qCqo2W0recNM="

printf \
"

   ____                  _   _               ___  
  / __ \                | | (_)             |__ \ 
 | |  | |_   _  ___  ___| |_ _  ___  _ __      ) |
 | |  | | | | |/ _ \/ __| __| |/ _ \| '_ \    / / 
 | |__| | |_| |  __/\__ \ |_| | (_) | | | |  / /_ 
  \___\_\\\\\\__,_|\___||___/\__|_|\___/|_| |_| |____|
                                                  
                                                  

Verify the signature by this address over this message.

=========================================

Address: $address
Message: $message
Signature: $signature

=========================================

"

output=$(curl -s https://bitcoin-mainnet.g.allthatnode.com/archive/json_rpc \
--request POST \
--header "Content-Type: text/plain" \
--data "{ 
  \"jsonrpc\": \"1.0\", 
  \"id\": \"0\", 
  \"method\": \"verifymessage\", 
  \"params\": [\"$address\",\"$signature\",\"$message\"] 
}")

result=$(echo $output | jq -r '.result')
error=$(echo $output | jq -r '.error')

if [ "$error" != "null" ]
then
  echo "Something went wrong: $error"
  exit 1
fi

printf "Result: $result\n"



