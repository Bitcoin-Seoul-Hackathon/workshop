import requests
from bitcoin import ecdsa_verify
import json

# Q1 & Q2
# RPC endpoint와 블록 번호
rpc_url = "https://bitcoin-testnet.drpc.org"
block_x_number = 2817654

# RPC 호출 헬퍼 함수
def rpc_call(method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params if params else [],
        "id": 1
    }
    response = requests.post(rpc_url, json=payload).json()
    return response.get('result', None)

# 1. Block X의 해시 값 얻기
block_x_hash = rpc_call("getblockhash", [block_x_number])
print("Q1")
print(f"Hash of Block X: {block_x_hash}")

# 2. 주소와 메시지에 대한 서명 검증
address = "1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
message = "1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
signature = "HCsBcgB+Wcm8kOGMH8IpNeg0H4gjCrlqwDf/GlSXphZGBYxm0QkKEPhh9DTJRp2IDNUhVr0FhP9qCqo2W0recNM="

def verify_signature(address, message, signature):
    try:
        verified = ecdsa_verify(message, signature, address)
        return verified
    except Exception as e:
        return False

is_signature_valid = verify_signature(address, message, signature)
print("Q2")
print(f"Signature valid: {is_signature_valid}")

# 3. Block Y에 의해 생성된 새로운 출력 수 얻기
block_y_number = block_x_number + 1
block_y_hash = rpc_call("getblockhash", [block_y_number])
block_y_data = rpc_call("getblock", [block_y_hash, 2])

# block_y_data의 구조를 확인하기 위해 출력
# print("Block Y Data:", json.dumps(block_y_data, indent=2))

# block_y_data가 문자열로 반환되었는지 확인하고 파싱
if isinstance(block_y_data, str):
    block_y_data = json.loads(block_y_data)

# 새 출력 수 계산

new_outputs_count = sum(len(tx['vout']) for tx in block_y_data['tx'])
print("Q3")
print(f"Number of new outputs created by Block Y: {new_outputs_count}")

# Q3
import requests
from bitcoin import ecdsa_verify
import json

# RPC endpoint와 블록 번호
rpc_url = "https://bitcoin-testnet.drpc.org"
block_x_number = 2817654

# RPC 호출 헬퍼 함수
def rpc_call(method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params if params else [],
        "id": 1
    }
    response = requests.post(rpc_url, json=payload).json()
    return response.get('result', None)

# 1. Block X의 해시 값 얻기
block_x_hash = rpc_call("getblockhash", [block_x_number])
print(f"Hash of Block X: {block_x_hash}")

# 2. 주소와 메시지에 대한 서명 검증
address = "1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
message = "1E9YwDtYf9R29ekNAfbV7MvB4LNv7v3fGa"
signature = "HCsBcgB+Wcm8kOGMH8IpNeg0H4gjCrlqwDf/GlSXphZGBYxm0QkKEPhh9DTJRp2IDNUhVr0FhP9qCqo2W0recNM="

def verify_signature(address, message, signature):
    try:
        verified = ecdsa_verify(message, signature, address)
        return verified
    except Exception as e:
        return False

is_signature_valid = verify_signature(address, message, signature)
print(f"Signature valid: {is_signature_valid}")

# Q4

# what is BIP 32
print("Q4")
print("What is BIP 32?")
print("BIP32, or Bitcoin Improvement Proposal 32, introduces the concept of hierarchical deterministic (HD) wallets. These wallets generate a tree of key pairs from a single seed, allowing users to manage multiple addresses and private keys from one master key. This structure facilitates simplified backups, as only the master seed needs to be saved. It also enhances privacy by allowing different addresses for each transaction. BIP32's deterministic nature ensures the same set of keys can be regenerated from the seed, ensuring continuity even if the wallet is lost, provided the seed is securely stored.")
# BIP32, or Bitcoin Improvement Proposal 32, introduces the concept of hierarchical deterministic (HD) wallets.
# These wallets generate a tree of key pairs from a single seed,
# allowing users to manage multiple addresses and private keys from one master key.
# This structure facilitates simplified backups, as only the master seed needs to be saved.
# It also enhances privacy by allowing different addresses for each transaction.
# BIP32's deterministic nature ensures the same set of keys can be regenerated from the seed,
# ensuring continuity even if the wallet is lost, provided the seed is securely stored.