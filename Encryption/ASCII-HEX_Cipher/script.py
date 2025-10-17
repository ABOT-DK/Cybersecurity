
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


# ---------------------------
# Main Functional Element
# ---------------------------

class AsciiHexCipher:
    def __init__(self):
        print(Fore.YELLOW + "ASCIIHEXCIPHER ready!\n")

    def encrypt(self, text):
        hex_result = text.encode("ascii").hex()
        return hex_result.upper()
    
    def decrypt(self, hex_text):
        try:
            ascii_result = bytes.fromhex(hex_text).decode("ascii")
            return ascii_result
        except ValueError:
            return "Invalid hexadecimal input."


# ---------------------------
# Menu Section
# ---------------------------

def main():
    print("")
    print("< ============================= >")
    print("")
    cipher = AsciiHexCipher()
    
    while True:
        print("< ============================= >")
        print("")
        print(Fore.YELLOW + "Choose an option:")
        print(Fore.YELLOW + "1. Encrypt ASCII to Hexadecimal")
        print(Fore.YELLOW + "2. Decrypt Hexadecimal to ASCII")
        print(Fore.YELLOW + "3. Exit")
        print("")
        print("< ============================= >")
        print("")
        print("")
        print("")


        choice = input(Fore.CYAN + "Choose what you want to do today: ").strip()
        
        if choice == "1":
            text = input("Enter text to encrypt: ")
            encrypted = cipher.encrypt(text)
            print(Fore.GREEN + f"Encrypted (Hex): {encrypted}\n")
        
        elif choice == "2":
            hex_text = input("Enter hex text to decrypt: ")
            decrypted = cipher.decrypt(hex_text)
            print(Fore.GREEN + f"Decrypted (ASCII): {decrypted}\n")
        
        elif choice == "3":
            print("Goodbye ...")
            break
        
        else:
            print(Fore.RED + "Invalid choice. Please try again.\n")


# ---------------------------
# Run the program
# ---------------------------

if __name__ == "__main__":
    main()