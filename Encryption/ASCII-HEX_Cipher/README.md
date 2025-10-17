# ASCII–Hexadecimal Cipher

The **ASCII–Hexadecimal Cipher** is a simple Python-based command-line tool that allows you to:
- **Encrypt** plain ASCII text into **Hexadecimal format**  
- **Decrypt** Hexadecimal strings back into **ASCII text**

This project demonstrates **Object-Oriented Programming (OOP)**, **data encoding**, and **user interaction** in Python.  
It’s a beginner-friendly introduction to how text data can be represented and transformed between formats in computer systems.

---

## 💡 Why You Need It
When dealing with cybersecurity, networking, or low-level programming, data is often stored or transmitted in **encoded formats** such as:
- **ASCII** → character encoding (used to represent readable text)
- **Hexadecimal** → binary-to-text encoding (used for compact, safe representation)

Understanding how to convert between these formats helps you:
- Read and write encoded data in tools like Wireshark, Burp Suite, or hex editors  
- Learn how computers interpret and store text  
- Build a foundation for cryptography and encoding systems  

This tool makes those conversions **easy to experiment with**.

---

##  Usage

### 🔧 Prerequisites
You need **Python 3.x** installed on your system.  
Install the optional `colorama` library for colorful terminal output:

---

## Example Conversion Table

| Character | ASCII (Decimal) | Hexadecimal |
|------------|-----------------|--------------|
| H | 72 | 48 |
| E | 69 | 45 |
| L | 76 | 4C |
| O | 79 | 4F |

---

## Example Output (Bash)

$ python script.py

< ============================= >"

ASCIIHEXCIPHER ready!

< ============================= >

Choose an option:
1. Encrypt ASCII to Hexadecimal
2. Decrypt Hexadecimal to ASCII
3. Exit

< ============================= >

Choose what you want to do today: 1
Enter text to encrypt: HELLO
Encrypted (Hex): 48454C4C4F

< ============================= >

Choose an option:
1. Encrypt ASCII to Hexadecimal
2. Decrypt Hexadecimal to ASCII
3. Exit

< ============================= >

Choose what you want to do today: 2
Enter hex text to decrypt: 48454C4C4F
Decrypted (ASCII): HELLO

< ============================= >

Choose an option:
1. Encrypt ASCII to Hexadecimal
2. Decrypt Hexadecimal to ASCII
3. Exit

< ============================= >

Goodbye...