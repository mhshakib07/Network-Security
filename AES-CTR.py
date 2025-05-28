from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# AES-CTR Encryption
def aes_ctr_encrypt(plaintext, key, nonce):
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# AES-CTR Decryption
def aes_ctr_decrypt(ciphertext, key, nonce):
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Example Usage
if __name__ == "__main__":
    # Key (must be 16, 24, or 32 bytes for AES)
    key = get_random_bytes(16)  # 128-bit key
    # Nonce (must be unique for each encryption)
    nonce = get_random_bytes(8)  # 64-bit nonce
    # Plaintext (data to encrypt)
    plaintext = b"HelloWorld123456"

    # Print the original plaintext
    print(f"Original Plaintext: {plaintext.decode()}")

    # Encrypt
    ciphertext = aes_ctr_encrypt(plaintext, key, nonce)
    print(f"Ciphertext (hex): {ciphertext.hex()}")

    # Decrypt
    decrypted_text = aes_ctr_decrypt(ciphertext, key, nonce)
    print(f"Decrypted Plaintext: {decrypted_text.decode()}")