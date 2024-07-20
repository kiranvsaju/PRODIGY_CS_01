def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_message += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_message += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_message += chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            elif char.isupper():
                decrypted_message += chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
        else:
            decrypted_message += char
    return decrypted_message

def main():
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? (q to quit): ").lower()
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()
