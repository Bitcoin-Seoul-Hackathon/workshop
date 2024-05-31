import requests
from bitcoin import ecdsa_verify
import json

# Q1 & Q2
# RPC endpoint와 블록 번호
rpc_url = "https://bitcoin-testnet.drpc.org"
block_x_number = 2817671

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
block_x_number = 2817671

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

# what is BIP 31
print("Q4")
print("What is BIP 31?")
print('BIP31, or Bitcoin Improvement Proposal 31, introduces a new message type called "PONG" to the Bitcoin protocol. It is designed to enhance the peer-to-peer (P2P) network by improving the "PING" message functionality. Previously, PING messages were used to check if a node was responsive, but they lacked a response mechanism. With BIP31, when a node receives a PING message, it responds with a PONG message, which includes the nonce sent in the original PING. This change allows nodes to verify the responsiveness and round-trip time of their connections more effectively, enhancing network reliability and performance.')