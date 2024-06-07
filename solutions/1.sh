#!/bin/bash

block_number=2817692

printf \
"
   ____                  _   _               __ 
  / __ \                | | (_)             /_ |
 | |  | |_   _  ___  ___| |_ _  ___  _ __    | |
 | |  | | | | |/ _ \/ __| __| |/ _ \| '_ \   | |
 | |__| | |_| |  __/\__ \ |_| | (_) | | | |  | |
  \___\_\\__,_|\___||___/\__|_|\___/|_| |_|  |_|
                                                
                                                

What is the hash of block $block_number?

=========================================

"

block_hash=$(curl -s "https://api.blockcypher.com/v1/btc/test3/blocks/$block_number" | jq -r '.hash')

printf "Hash of Block $block_number is $block_hash.\n"

printf "=========================================\n"