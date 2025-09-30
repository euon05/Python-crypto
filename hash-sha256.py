from cryptography.hazmat.primitives import hashes

message = 'hash test. 해시함수 테스트'
print("Message:", message)

# 1. SHA1 해시 계산
digest = hashes.Hash(hashes.SHA1())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA1 해시(hex):", hash_value.hex())

# 2. SHA224 해시 계산
digest = hashes.Hash(hashes.SHA224())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA-224 해시(hex):", hash_value.hex())

# 3. SHA256 해시 계산
digest = hashes.Hash(hashes.SHA256())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA-256 해시(hex):", hash_value.hex())

# 4. SHA384 해시 계산
digest = hashes.Hash(hashes.SHA384())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA-384 해시(hex):", hash_value.hex())

# 5. SHA512 해시 계산
digest = hashes.Hash(hashes.SHA512())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA-512 해시(hex):", hash_value.hex())

# 6. SHA512_224 해시 계산
digest = hashes.Hash(hashes.SHA512_224())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA-512_224 해시(hex):", hash_value.hex())

# 7. SHA512_256 해시 계산
digest = hashes.Hash(hashes.SHA512_256())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA-512_256 해시(hex):", hash_value.hex())

# 8. BLAKE2b 해시 계산
digest = hashes.Hash(hashes.BLAKE2b(64))
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("BLAKE2b(64) 해시(hex):", hash_value.hex())

# 9. BLAKE2s 해시 계산
digest = hashes.Hash(hashes.BLAKE2s(32))
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("BLAKE2s(32) 해시(hex):", hash_value.hex())

# 10. SHA3_224 해시 계산
digest = hashes.Hash(hashes.SHA3_224())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA3_224 해시(hex):", hash_value.hex())

# 11. SHA3_256 해시 계산
digest = hashes.Hash(hashes.SHA3_256())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA3_256 해시(hex):", hash_value.hex())

# 12. SHA3_384 해시 계산
digest = hashes.Hash(hashes.SHA3_384())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA3_384 해시(hex):", hash_value.hex())

# 13. SHA3_512 해시 계산
digest = hashes.Hash(hashes.SHA3_512())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHA3_512 해시(hex):", hash_value.hex())

# 14. SHAKE128 해시 계산
digest = hashes.Hash(hashes.SHAKE128(32))
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHAKE128 해시(hex):", hash_value.hex())

# 15. SHAKE256 해시 계산
digest = hashes.Hash(hashes.SHAKE256(32))
digest.update(message.encode('utf-8'))
hash_value = digest.finalize()
print("SHAKE256 해시(hex):", hash_value.hex())
