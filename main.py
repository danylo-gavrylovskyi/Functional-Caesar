def encrypt(rawText: str, key: int) -> str:
    result: str = ''
    for char in rawText:
        if char == '\0': break

        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr(((ord(char) - ord(base) + key) % 26) + ord(base))
        else:
            result += chr((ord(char) + key) % 68)
        
    return result

def decrypt(encryptedText: str, key: int) -> str:
    result: str = ''
    for char in encryptedText:
        if char == '\0': break

        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr(((ord(char) - ord(base) - key + 26) % 26) + ord(base))
        else:
            result += chr((ord(char) - key) % 68)
        
    return result

def main():
    choice: int
    while True:
        print("Choose the command\n\t0. Exit\n\t1. Encrypt text\n\t2. Decrypt text")
        choice = int(input(">> "))
        
        if (choice == 0): break
        match choice:
            case 1:
                fileNameToLoad: str = input("Enter the file name for loading: ")
                fileNameToSave: str = input("Enter the file name for saving: ")
                key: int = int(input("Enter the key: "))

                textToEncrypt: str = open(fileNameToLoad).read()
                encryptedText: str = encrypt(textToEncrypt, key)
                open(fileNameToSave, 'w').write(encryptedText)

                print(f"Encrypted text: {encryptedText}")
            case 2:
                fileNameToLoad: str = input("Enter the file name for loading: ")
                fileNameToSave: str = input("Enter the file name for saving: ")
                key: int = int(input("Enter the key: "))

                textToDecrypt: str = open(fileNameToLoad).read()
                decryptedText: str = decrypt(textToDecrypt, key)
                open(fileNameToSave, 'w').write(decryptedText)

                print(f"Decrypted text: {decryptedText}")

if __name__ == '__main__':
    main()
