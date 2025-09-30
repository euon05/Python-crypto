import base64
import os
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.exceptions import InvalidSignature

# 1. CMAC 생성
key = os.urandom(16)  # 16바이트 랜덤 키 생성
message = 'Message to authenticate 메시지인증코드 테스트'

c = cmac.CMAC(algorithms.AES(key))
c.update(message.encode('utf-8'))
signature = c.finalize()

print('Key: ', base64.b64encode(key).decode())
print('Message: ', message)
print('MAC: ', signature.hex())

# 2. CMAC 검증
try:
    c = cmac.CMAC(algorithms.AES(key))
    c.update(message.encode('utf-8'))
    c.verify(signature)
    print("검증 성공")
except InvalidSignature:
    print("검증 실패: 서명이 유효하지 않습니다.")
