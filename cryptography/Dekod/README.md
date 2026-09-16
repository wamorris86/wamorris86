# Dekod

Dekod is a cryptography multi-tool written in Python for CTF players, pentesters, and security professionals

No external dependencies aside from standard Python library

### Supported Algorithms
**Encoding/Decoding**
 - Base64
 - Hex
 - Binary
 - URL

**Ciphers**
 - Caesar (cipher, decipher, brute force)
 - ROT13
 - Atbash  
 - XOR
 - Vigenere


# Installing  

#### For linux users:
1. Download the raw dekod.py file
2. Rename dekod.py (optional):  
`mv dekod.py dekod`
3. Make dekod executable:  
`sudo chmod +x dekod`
4. Copy dekod to /usr/local/bin:  
`sudo cp dekod /usr/local/bin`

Now dekod can be called simply with `dekod` from anywhere!

#### For Windows users:
Windows users can run Dekod from the directory it's in with `python3 dekod.py`, or add the directory to PATH to call it from anywhere.

# Usage
***Dekod supports CLI mode along with its normal, graphical mode.***

**GUI Mode**

`python3 dekod.py`*

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

              ██████╗ ███████╗██╗  ██╗ ██████╗ ██████╗ 
              ██╔══██╗██╔════╝██║ ██╔╝██╔═══██╗██╔══██╗
              ██║  ██║█████╗  █████╔╝ ██║   ██║██║  ██║
              ██║  ██║██╔══╝  ██╔═██╗ ██║   ██║██║  ██║
              ██████╔╝███████╗██║  ██╗╚██████╔╝██████╔╝
              ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
-------------------- A cryptographic multi-tool --------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://github.com/wamorris86/wamorris86/tree/main/cryptography/Dekod
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 -- Please select an algorithm -- 

type '?' or 'help' for help

1. Base64
2. Hex
3. Binary
4. URL
5. Caesar
6. ROT13
7. Atbash
8. XOR
9. Vigenere
10. Exit

>>>
```

**CLI Mode:**

`python3 dekod.py -h`*

       -h, --help
       -m, --method METHOD  algorithm (base64, hex, binary, url, rot13, caesar, atbash, xor, vigenere)
       -e, --encode         encode mode
       -d, --decode         decode mode
       -b, --brute          brute force mode (caesar only)
       -k, --key KEY        key for caesar/xor  

`python3 dekod.py -m [method] [-e] [-d] [-b] [-k key] [string]`*  

Example: `python3 dekod.py -m base64 -e 'Hello World!'`*  
Result: Encoded: SGVsbG8gV29ybGQh

*you can skip out on using `python3 dekod.py`, see [Installing](#installing)


> Dekod is a work in progress - more algorithms coming soon
