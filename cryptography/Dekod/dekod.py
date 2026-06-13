import os
import sys
import base64
import codecs
import urllib.parse

def base64_encode(data):
    encoded_data = base64.b64encode(data.encode()).decode()
    print(f"\nEncoded: {encoded_data}")

def base64_decode(data):
    decoded_data = base64.b64decode(data.encode()).decode()
    print(f"\nDecoded: {decoded_data}")

def hex_encode(data):
    encoded_data = codecs.encode(data.encode(), 'hex').decode()
    print(f"\nEncoded: {encoded_data}")

def hex_decode(data):
    decoded_data = bytes.fromhex(data).decode()
    print(f"\nDecoded: {decoded_data}")

def binary_encode(data):
    encoded_data = ' '.join(format(ord(c), '08b') for c in data)
    print(f"\nEncoded: {encoded_data}")

def binary_decode(data):
    decoded_data = ''.join(chr(int(b, 2)) for b in data.split())
    print(f"\nDecoded: {decoded_data}")

def url_encode(data):
    encoded_data = urllib.parse.quote(data)
    print(f"\nEncoded: {encoded_data}")

def url_decode(data):
    decoded_data = urllib.parse.unquote(data)
    print(f"\nDecoded: {decoded_data}")

def rot13_cipher(data):
    encoded_data = codecs.encode(data, "rot13")
    print(f"Encoded: {encoded_data}")

def rot13_decipher(data):
    decoded_data = codecs.decode(data, "rot13")
    print(f"Decoded: {decoded_data}")

def get_method():
    while True:
        method = input("(E)ncode or (D)ecode?: ").lower()
        if method in ["e", "d"]:
            return method
        print("\033[1m\033[31m -- Invalid option -- \033[0m")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

ALGORITHMS = {
    "1": ("Base64", base64_encode, base64_decode),
    "2": ("Hex", hex_encode, hex_decode),
    "3": ("Binary", binary_encode, binary_decode),
    "4": ("URL", url_encode, url_decode),
#    "5": ("Caesar", caesar_cipher, caesar_decipher),
#    "6": ("ROT13", rot13_cipher, rot13_decipher),
#    "7": ("Atbash", atbash_cipher, atbash_decipher), 
}

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("--------------- Dekod, an all in one encoder/decoder ---------------")
    print("https://github.com/wamorris86/wamorris86/tree/main/cryptography/dekod")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        print("\n -- Please select an algorithm -- \n")
        for k, v in ALGORITHMS.items():
            print(f"{k}. {v[0]}")
        print(f"{len(ALGORITHMS)+1}. Exit")
        
        choice = input("\n>>>  ")
        clear()
        if choice == str(len(ALGORITHMS)+1):
            sys.exit()
        elif choice in ALGORITHMS:
            method = get_method()
            data = input("\nEnter string: ")
            ALGORITHMS[choice][1](data) if method == "e" else ALGORITHMS[choice][2](data)
            again = input("\nContinue? (Y/N): ").lower()
            if again == "n":
                sys.exit()
        else:
            clear()
            print("\033[1m\033[31m -- Invalid option -- \033[0m")

main()