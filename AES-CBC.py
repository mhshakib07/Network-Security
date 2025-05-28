from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# AES-CBC Encryption
def aes_cbc_encrypt(plaintext, key):
    # Generate a random 128-bit (16-byte) IV
    iv = get_random_bytes(16)
    # Create AES-CBC cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Encrypt the plaintext (padding to block size)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return iv + ciphertext  # Return IV + ciphertext

# AES-CBC Decryption
def aes_cbc_decrypt(ciphertext, key):
    # Extract the IV (first 16 bytes)
    iv = ciphertext[:16]
    # Extract the actual ciphertext
    ciphertext = ciphertext[16:]
    # Create AES-CBC cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the ciphertext and unpad
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Example Usage
if __name__ == "__main__":
    # Key (must be 16, 24, or 32 bytes for AES)
    key = get_random_bytes(16)  # 128-bit key
    # Plaintext (data to encrypt)
    plaintext = b"Hello, World!"

    # Print the original plaintext
    print(f"Original Plaintext: {plaintext.decode()}")

    # Encrypt
    encrypted_data = aes_cbc_encrypt(plaintext, key)
    print(f"Ciphertext (hex): {encrypted_data.hex()}")

    # Decrypt
    decrypted_text = aes_cbc_decrypt(encrypted_data, key)
    print(f"Decrypted Plaintext: {decrypted_text.decode()}")