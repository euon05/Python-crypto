import base64
import os
from cryptography.hazmat.primitives import poly1305
from cryptography.exceptions import InvalidSignature

# 1. MAC 생성
key = os.urandom(32)  # 32바이트 키
message = 'Message to authenticate 메시지인증코드 테스트'
p = poly1305.Poly1305(key)
p.update(message.encode('utf-8'))
signature = p.finalize()
print('Key: ',base64.b64encode(key).decode())
print('Message: ', message)
print('mac: ', signature.hex())


# 2. MAC 검증
#poly1305 MAC 검증
try:
    mac_verify = poly1305.Poly1305(key)
    mac_verify.update(message)
    mac_verify.verify(signature)
    print("검증 성공")
except InvalidSignature:
    print("검증 실패: 서명이 유효하지 않습니다.")
