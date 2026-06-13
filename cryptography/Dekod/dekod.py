# Dekod is a cryptography multi-tool written in Python.
# It supports: Base64, Hex, Binary, URL, ROT13, Caesar, Atbash
# Dekod is a work in progress, but there are many more features coming in the future

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
    print(f"Result: {encoded_data}")

# normalize to 0-25, shift, wrap with mod 26, add base back
def caesar_cipher(data):
    shift = int(input("Enter Shift: "))
    result = ""
    for char in data:
        if char.isupper():
            shifted = (ord(char) - 65 + shift) % 26
            result += chr(shifted + 65)
        elif char.islower():
            shifted = (ord(char) - 97 + shift) % 26
            result += chr(shifted + 97)
        else:
            result += char
    print(result)

def caesar_decipher(data):
    shift = int(input("Enter shift: "))
    result = ""
    for char in data:
        if char.isupper():
            shifted = (ord(char) - 65 - shift) % 26
            result += chr(shifted + 65)
        elif char.islower():
            shifted = (ord(char) - 97 - shift) % 26
            result += chr(shifted + 97)
        else:
            result += char
    print(result)

# normalizes to 0-25, goes through all shifts (1-26), prints all results
def caesar_brute(data):
    for shift in range(1, 26):
        result = ""
        for char in data:
            if char.isupper():
                shifted = (ord(char) - 65 + shift) % 26
                result += chr(shifted + 65)
            elif char.islower():
                shifted = (ord(char) - 97 + shift) % 26
                result += chr(shifted + 97)
            else:
                result += char
        print(f"Shift {shift}: {result}")

def atbash_cipher(data):
    result = ""
    for char in data:
        if char.isupper():
            mirrored = ord('Z') - (ord(char) - ord('A'))
            result += chr(mirrored)
        elif char.islower():
            mirrored = ord('z') - (ord(char) - ord('a'))
            result += chr(mirrored)
        else:
            result += char
    print(result)


def get_method():
    while True:
        method = input("(E)ncode or (D)ecode?: ").lower()
        if method in ["e", "d"]:
            return method
        print("\033[1m\033[31m -- Invalid option -- \033[0m")

def prompt_continue():
    again = input("\nContinue? (Y/N): ").lower()
    if again == "n":
        sys.exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# (name, encode_fn, decode_fn)
ALGORITHMS = {
    "1": ("Base64", base64_encode, base64_decode),
    "2": ("Hex", hex_encode, hex_decode),
    "3": ("Binary", binary_encode, binary_decode),
    "4": ("URL", url_encode, url_decode),
    "5": ("Caesar", caesar_cipher, caesar_decipher, caesar_brute),
    "6": ("ROT13", rot13_cipher),
    "7": ("Atbash", atbash_cipher), 
}

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("--------------- Dekod, an all in one encoder/decoder ---------------")
    print("https://github.com/wamorris86/wamorris86/tree/main/cryptography/Dekod")
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

        elif choice == "5":
            while True:
                method = input("(E)ncode, (D)ecode, or (B)rute force?: ").lower()
                if method in ["e", "d", "b"]:
                    break
                print("\033[1m\033[31m -- Invalid option -- \033[0m")
            data = input("\nEnter string: ")
            if method == "e":
                caesar_cipher(data)
            elif method == "d":
                caesar_decipher(data)
            else:
                caesar_brute(data)
            prompt_continue()

        elif choice == "6":
            data = input("\nEnter string: ")
            rot13_cipher(data)
            prompt_continue()
        
        elif choice == "7":
            data = input("\nEnter string: ")
            atbash_cipher(data)
            prompt_continue()

        elif choice in ALGORITHMS:
            method = get_method()
            data = input("\nEnter string: ")
            ALGORITHMS[choice][1](data) if method == "e" else ALGORITHMS[choice][2](data)
            prompt_continue()

        else:
            clear()
            print("\033[1m\033[31m -- Invalid option -- \033[0m")

main()