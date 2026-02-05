import base64
import sys

def decode_base64_to_txt(input_file, output_file):
    # Open the encoded file
    with open(input_file, "rb") as f:
        encoded_bytes = f.read()

    # Decode to Base64
    decoded_bytes = base64.b64decode(encoded_bytes)

    # Write Base64 output to a new file
    with open(output_file, "wb") as f:
        f.write(decoded_bytes)

    print(f"Decoded file saved as: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decode.py <encoded.txt> <decoded.txt>")
        sys.exit(1)

    decode_base64_to_txt(sys.argv[1], sys.argv[2])
