from cryptography.hazmat.primitives import hashes, hmac
from cryptography.exceptions import InvalidSignature

#1. hmac 생성
key = 'secretkey'.encode('utf-8')
message = 'message to hash 메시지 인증 코드 테스트'
h = hmac.HMAC(key,hashes.SHA256())
h.update(message.encode('utf-8'))
signature = h.finalize()
print('Key: ',key)
print("Message: ",message)
print('HMAc:',signature.hex())

#hmac 검증
#에러 처리를 위해 try/except구문을 사용합니다
try:
  h = hmac.HMAC(key,hashes.SHA256())
  h.update(message.encode('utf-8'))
  h.verify(signature)
  print("\검증성공")
except InvalidSignature:
  print("\검증실패: 서명이 유효하지 않습니다.")
