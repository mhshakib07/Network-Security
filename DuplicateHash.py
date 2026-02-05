import hashlib  

def file_hash(filename):

    h = hashlib.sha256()          # Create a SHA-256 hash object
    with open(filename, "rb") as f:  # Open file in binary read mode
        h.update(f.read())        # Read file content and update hash
    return h.hexdigest()          # Return hash value in hexadecimal format

# Take input
file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")

# Generate hash values for both files
hash1 = file_hash(file1)
hash2 = file_hash(file2)

# Compare the hash values
if hash1 == hash2:
    print("Both files have identical content.")
else:
    print("Files are different.")
