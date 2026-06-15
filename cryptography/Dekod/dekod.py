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
    rot13_result = codecs.encode(data, "rot13")
    print(f"Result: {rot13_result}")

# normalize to 0-25, shift, wrap with mod 26, add base back
def caesar_cipher(data):
    shift = get_shift()
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
    shift = get_shift()
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
                shifted = (ord(char) - 65 - shift) % 26
                result += chr(shifted + 65)
            elif char.islower():
                shifted = (ord(char) - 97 - shift) % 26
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

def xor_cipher(data):
    print("Placeholder")

def vigenere_cipher(data):
    print("Placeholder")

def get_method():
    while True:
        method = input("(E)ncode or (D)ecode?: ").lower()
        if method in ["e", "d"]:
            return method
        print("\033[1m\033[31m -- Invalid option -- \033[0m")

# asks if user would like to continue after each use
def prompt_continue():
    again = input("\nContinue? (Y/N): ").lower()
    if again == "n":
        sys.exit()

# takes input and reprompts if user supplies empty input
def get_input(prompt):
    while True:
        data = input(prompt)
        if data.strip():
            return data
        print("\033[1m\033[31m -- Input cannot be empty -- \033[0m")

# takes shift from user and reprompts if no input is given
def get_shift():
    while True:
        try:
            shift = int(input("Enter Shift: "))
            return shift
        except ValueError:
            print("\033[1m\033[31m -- Shift must be a number -- \033[0m")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ("name", encode_fn, decode_fn, "description")
# description is shown as each function is initially called
# some functions (like caesar, rot13, atbash) have their own function within main() to account for different dict entries
ALGORITHMS = {
    "1": ("Base64", base64_encode, base64_decode, "Base64 encodes binary data as ASCII text, commonly used to transfer data over text-based protocols."),
    "2": ("Hex", hex_encode, hex_decode, "Hex represents each byte as two hex digits (0-9, A-F)"),
    "3": ("Binary", binary_encode, binary_decode, "Binary translates data into sequences of 1s and 0s, which computers use to process and store information."),
    "4": ("URL", url_encode, url_decode, "URL encoding translates special characters into safe, universally accepted ASCII format"),
    "5": ("Caesar", caesar_cipher, caesar_decipher, caesar_brute),
    "6": ("ROT13", rot13_cipher),
    "7": ("Atbash", atbash_cipher),
#    "8": ("XOR", xor_cipher),
#    "9": ("Vigenere", vigenere_cipher)
}

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("----------------- Dekod, a cryptographic multi-tool -----------------")
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
            print("\n\033[2mCaesar Cipher (shift cipher) is an encryption technique that shifts each letter in a message by a fixed number of positions down the alphabet.\033[0m\n")
            while True:
                method = input("(E)ncrypt, (D)ecrypt, or (B)rute force?: ").lower()
                if method in ["e", "d", "b"]:
                    break
                print("\033[1m\033[31m -- Invalid option -- \033[0m")
            data = get_input("\nEnter string: ")
            if method == "e":
                caesar_cipher(data)
            elif method == "d":
                caesar_decipher(data)
            else:
                caesar_brute(data)
            prompt_continue()

        elif choice == "6":
            print("\n\033[2mROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter AFTER it in the alphabet.\033[0m\n")
            data = get_input("\nEnter string: ")
            rot13_cipher(data)
            prompt_continue()

        elif choice == "7":
            print("\n\033[2mAtbash is a simple substitusion cipher that simply reverses the alphabet, for example, every instance of (A) is replaced with (Z).\033[0m\n")
            data = get_input("\nEnter string: ")
            atbash_cipher(data)
            prompt_continue()

        elif choice in ALGORITHMS:
            print(f"\n\033[2m{ALGORITHMS[choice][3]}\033[0m\n")
            method = get_method()
            data = get_input("\nEnter string: ")
            ALGORITHMS[choice][1](data) if method == "e" else ALGORITHMS[choice][2](data)
            prompt_continue()

        else:
            clear()
            print("\033[1m\033[31m -- Invalid option -- \033[0m")

main()