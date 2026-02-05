import base64
import sys

def encode_txt_to_base64(input_file, output_file):
    # Open the text file in binary mode
    with open(input_file, "rb") as f:
        file_bytes = f.read()

    # Encode to Base64
    encoded_bytes = base64.b64encode(file_bytes)

    # Write Base64 output to a new file
    with open(output_file, "wb") as f:
        f.write(encoded_bytes)

    print(f"Base64 encoded file saved as: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encode.py <input.txt> <output.txt>")
        sys.exit(1)

    input_txt = sys.argv[1]
    output_txt = sys.argv[2]

    encode_txt_to_base64(input_txt, output_txt)
