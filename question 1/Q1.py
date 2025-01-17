import string

# Function to encrypt the content of a file and save it to another file
def encrypt_file(input_file, output_file, n, m):
    # Helper function to encrypt a single character
    def encrypt_char(char):
        if char in string.ascii_lowercase:  # For lowercase letters
            if char <= 'm':  # First half of the alphabet (a-m)
                return chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
            else:  # Second half of the alphabet (n-z)
                return chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))
        elif char in string.ascii_uppercase:  # For uppercase letters
            if char <= 'M':  # First half of the alphabet (A-M)
                return chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
            else:  # Second half of the alphabet (N-Z)
                return chr(((ord(char) - ord('A') + m**2) % 26) + ord('A'))
        else:  # For non-alphabetic characters, keep them unchanged
            return char

    # Read the content of the input file
    with open(input_file, 'r') as file:
        raw_text = file.read()

    # Encrypt the content using the helper function
    encrypted_text = ''.join(encrypt_char(c) for c in raw_text)

    # Write the encrypted content to the output file
    with open(output_file, 'w') as file:
        file.write(encrypted_text)

# Function to decrypt the content of a file and save it to another file
def decrypt_file(input_file, output_file, n, m):
    # Helper function to decrypt a single character
    def decrypt_char(char):
        if char in string.ascii_lowercase:  # For lowercase letters
            if char <= 'm':  # First half of the alphabet (a-m)
                return chr(((ord(char) - ord('a') - n * m) % 26) + ord('a'))
            else:  # Second half of the alphabet (n-z)
                return chr(((ord(char) - ord('a') + (n + m)) % 26) + ord('a'))
        elif char in string.ascii_uppercase:  # For uppercase letters
            if char <= 'M':  # First half of the alphabet (A-M)
                return chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            else:  # Second half of the alphabet (N-Z)
                return chr(((ord(char) - ord('A') - m**2) % 26) + ord('A'))
        else:  # For non-alphabetic characters, keep them unchanged
            return char

    # Read the content of the encrypted file
    with open(input_file, 'r') as file:
        encrypted_text = file.read()

    # Decrypt the content using the helper function
    decrypted_text = ''.join(decrypt_char(c) for c in encrypted_text)

    # Write the decrypted content to the output file
    with open(output_file, 'w') as file:
        file.write(decrypted_text)

# Function to verify if the decrypted text matches the original text
def verify_decryption(original_file, decrypted_file):
    # Read the content of the original file
    with open(original_file, 'r') as file:
        original_text = file.read()

    # Read the content of the decrypted file
    with open(decrypted_file, 'r') as file:
        decrypted_text = file.read()

    # Compare the original text with the decrypted text
    return original_text.strip() == decrypted_text.strip()

# Example usage
# Prompt user for input values for n and m
n = int(input("Enter the value of n (positive integer): "))
m = int(input("Enter the value of m (positive integer): "))

# Encrypt the content of "raw_text.txt" and save it to "encrypted_text.txt"
encrypt_file('raw_text.txt', 'encrypted_text.txt', n, m)

# Decrypt the content of "encrypted_text.txt" and save it to "decrypted_text.txt"
decrypt_file('encrypted_text.txt', 'decrypted_text.txt', n, m)

# Verify if the decrypted content matches the original content
if verify_decryption('raw_text.txt', 'decrypted_text.txt'):
    print("Decryption verified successfully.")
else:
    print("Decryption verification failed.")
