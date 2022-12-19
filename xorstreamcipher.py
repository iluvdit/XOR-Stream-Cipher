from typing import List, Tuple

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

def xor_encrypt(plaintext: str, key: str) -> str:
    # XOR the two input strings
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def encrypt_file(filename: str, key: str) -> None:
    # Open the input file and read the contents into a linked list
    with open(filename, "r") as f:
        data = f.read()
    head = None
    tail = None
    for ch in data:
        new_node = Node(ord(ch))
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    # Encrypt the data using the XOR function
    ciphertext = xor_encrypt(data, key)
    print("Ciphertext:", ciphertext)

    # Write the encrypted data to a new file
    with open(filename + ".encrypted", "w") as f:
        f.write(ciphertext)

def decrypt_file(filename: str, key: str) -> None:
    # Open the encrypted file and read the contents
    with open(filename, "r") as f:
        ciphertext = f.read()

    # Decrypt the data using the XOR function
    plaintext = xor_encrypt(ciphertext, key)

    # Write the decrypted data to a new file
    with open(filename + ".decrypted", "w") as f:
        f.write(plaintext)

def main() -> None:
    # Prompt the user for the input file and key
    filename = input("Enter the name of the file to encrypt: ")
    key = input("Enter the encryption key: ")

    # Encrypt the file
    encrypt_file(filename, key)

    # Decrypt the file
    decrypt_file(filename + ".encrypted", key)

if __name__ == "__main__":
    main()
