# workshop

**블록넘버: 2817678**

## 1. Block X의 해시 값은 무엇입니까 (what is the hash of block X) ?

("Block X"는 Bitcoin Testnet3 기준으로 아래의 \**참조 A, *참조 B를 참고하여 본인에게 매칭된 블록번호에 대한 블록 해시값을 찾아아 합니다.)

```bash
curl -X POST https://go.getblock.io/aa4e2b54b9f64572bd073be9c10fe34c \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "1.0",
    "id": "curltest",
    "method": "getblockhash",
    "params": [2817678]
  }'
```

**결과**

```
{"result":"000000000000000fbee264994dd048571a20344ea27dd0a599177ab5739c498e","error":null,"id":"curltest"}
```

**정답**: `000000000000000fbee264994dd048571a20344ea27dd0a599177ab5739c498e`

## 2. (참 / 거짓 파악),  다음 아래의 주소와 메시지에 대한 서명을 검증하세요(true / false) Verify the signature by this address over this message:

```
  주소(address): 1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa
	메세지(message): 1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa
	서명(signature): HCsBcgB+Wcm8kOGMH8IpNeg0H4gjCrlqwDf/GlSXphZGBYxm0QkKEPhh9DTJRp2IDNUhVr0FhP9qCqo2W0recNM=
```

https://www.verifybitcoinmessage.com/

여기서 invalid하다고 나옴

## 3. Block Y에 의해 생성된 새로운 출력은 몇 개인가요 (How many new outputs were created by block Y)?

("Block Y"는 "Block X + 1" 입니다. Bitcoin Testnet3 기준으로 아래의 \**참조 A, *참조 B를 참고하여 본인에게 매칭된 블록번호에 +1에 해당하는 블록 해시값을 찾아아 합니다.)

```
curl -X POST https://bitcoin-testnet.drpc.org/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "1.0",
    "id": "curltest",
    "method": "getblockhash",
    "params": [2817679]
  }'
```

**결과**

```
{"id":"curltest","jsonrpc":"2.0","result":"00000000e3d502084b128f1a12a78f6c56e8b2616fe55dbc4e35ff525ec31bea"}
```

```
curl -X POST https://bitcoin-testnet.drpc.org/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "1.0",
    "id": "curltest",
    "method": "getblock",
    "params": ["00000000e3d502084b128f1a12a78f6c56e8b2616fe55dbc4e35ff525ec31bea", 2]
  }'
```

**결과**

```json
{
  "id": "curltest",
  "jsonrpc": "2.0",
  "result": {
    "hash": "00000000e3d502084b128f1a12a78f6c56e8b2616fe55dbc4e35ff525ec31bea",
    "confirmations": 836,
    "height": 2817679,
    "version": 536870912,
    "versionHex": "20000000",
    "merkleroot": "984b0e526f2e352b1fe0308480259e8c25d96047a4ebfeb0f6e11e9bc42da97f",
    "time": 1716648293,
    "mediantime": 1716646001,
    "nonce": 2015418069,
    "bits": "1d00ffff",
    "difficulty": 1,
    "chainwork": "000000000000000000000000000000000000000000000debb8d6188277d1fce0",
    "nTx": 1,
    "previousblockhash": "000000000000000fbee264994dd048571a20344ea27dd0a599177ab5739c498e",
    "nextblockhash": "0000000093413342a1abed55e0f4f2cfe3cfe92b0861b83e8529372cb787ae1e",
    "strippedsize": 214,
    "size": 250,
    "weight": 892,
    "tx": [
      {
        "txid": "984b0e526f2e352b1fe0308480259e8c25d96047a4ebfeb0f6e11e9bc42da97f",
        "hash": "d622027aa818cd9c931b89bf0fa89d6984af96ebe5c2f7e721e45d4696386665",
        "version": 1,
        "size": 169,
        "vsize": 142,
        "weight": 568,
        "locktime": 0,
        "vin": [
          {
            "coinbase": "038ffe2a",
            "txinwitness": ["0000000000000000000000000000000000000000000000000000000000000000"],
            "sequence": 4294967295
          }
        ],
        "vout": [
          {
            "value": 0.00610351,
            "n": 0,
            "scriptPubKey": {
              "asm": "0 cc326e0ed5a9e8b470a4ebbbfe8901cbb2c68370",
              "desc": "addr(tb1qesexurk4485tgu9yawalazgpewevdqmsgwvmxt)#wn788udc",
              "hex": "0014cc326e0ed5a9e8b470a4ebbbfe8901cbb2c68370",
              "address": "tb1qesexurk4485tgu9yawalazgpewevdqmsgwvmxt",
              "type": "witness_v0_keyhash"
            }
          },
          {
            "value": 0.0,
            "n": 1,
            "scriptPubKey": {
              "asm": "OP_RETURN aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9",
              "desc": "raw(6a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9)#cav96mf3",
              "hex": "6a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9",
              "type": "nulldata"
            }
          }
        ],
        "hex": "010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff04038ffe2affffffff022f50090000000000160014cc326e0ed5a9e8b470a4ebbbfe8901cbb2c683700000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf90120000000000000000000000000000000000000000000000000000000000000000000000000"
      }
    ]
  }
}
```

vout이 2개의 원소를 가지므로, 답은 `2`.

## (보너스) 4. BIP31, 32, 33 중 선택하여 자유롭게 기술해주세요(Please choose one of BIP31, BIP32,or BIP33 and describe it freely).

BIP 31은 비트코인 네트워크에서 PING 메시지를 개선하는 제안이다. 이 제안은 노드 간의 연결 상태를 확인하기 위해 PING 메시지에 대한 응답으로 PONG 메시지를 정의한다. 이전에는 PING 메시지에 응답이 없어 노드 간의 연결 상태를 확인하기 어려웠다. BIP 31은 PING 메시지에 고유한 nonce를 포함하고, 이에 대응하는 PONG 메시지에서 동일한 nonce를 반환하도록 함으로써 노드 간의 연결 상태를 보다 효율적으로 모니터링할 수 있게 했다. 이를 통해 네트워크의 안정성과 신뢰성이 향상되었다.
