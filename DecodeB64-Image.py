import base64
import sys

def decode_base64_to_image(encoded_file, output_image):
    # Open Base64-encoded file in binary mode
    with open(encoded_file, "rb") as f:
        encoded_bytes = f.read()

    # Decode Base64 back to original image bytes
    image_bytes = base64.b64decode(encoded_bytes)

    # Write the decoded bytes to an image file
    with open(output_image, "wb") as img:
        img.write(image_bytes)

    print(f"Image decoded and saved as: {output_image}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decode_image.py <encoded.txt> <output_image>")
        sys.exit(1)

    decode_base64_to_image(sys.argv[1], sys.argv[2])
