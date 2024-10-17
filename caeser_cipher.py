
def caesar_cipher(message, shift):
    result = ""
    
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the letter is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char  # Keep non-letter characters unchanged (including numbers)
    
    return result


def main():
    print("Caesar Cipher")
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    message = input("Enter your message (you can include numbers): ")
    shift = int(input("Enter shift value (e.g., 3): "))
    
    # Adjust shift for decryption
    if choice == 'd':
        shift = -shift  # Negate the shift for decryption
    if choice == "d" or choice == "e":
            result = caesar_cipher(message, shift)
            action = "Encrypted" if choice == 'e' else "Decrypted"
            print(f"{action} message: {result}")
    else:
            print('**ALERT!!** select a valid ONE "e" or "d"!')

if __name__ == "__main__":
    main()
