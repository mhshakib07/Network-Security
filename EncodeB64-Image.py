import base64
import sys

def encode_image_to_base64(image_path, output_file):
    # Open image in binary mode
    with open(image_path, "rb") as img:
        image_bytes = img.read()

    # Encode image bytes to Base64
    encoded_bytes = base64.b64encode(image_bytes)

    # Write Base64 to output file
    with open(output_file, "wb") as f:
        f.write(encoded_bytes)

    print(f"Image encoded to Base64 and saved as: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encode_image.py <image_file> <output.txt>")
        sys.exit(1)

    encode_image_to_base64(sys.argv[1], sys.argv[2])
