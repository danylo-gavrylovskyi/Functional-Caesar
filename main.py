def encrypt(char: str, key: int) -> chr:
    if char.isalpha():
        base = 'A' if char.isupper() else 'a'
        return chr(((ord(char) - ord(base) + key) % 26) + ord(base))
    else:
        return chr((ord(char) + key) % 68)

def decrypt(char: str, key: int) -> chr:
    if char.isalpha():
        base = 'A' if char.isupper() else 'a'
        return chr(((ord(char) - ord(base) - key + 26) % 26) + ord(base))
    else:
        return chr((ord(char) - key) % 68)

def process_text(text: str, transformation, key: int) -> str:
    return ''.join(transformation(char, key) for char in text)

def main():
    while True:
        print("Choose the command\n\t0. Exit\n\t1. Encrypt text\n\t2. Decrypt text")
        choice: str = int(input(">> "))
        
        if choice == 0:
            break
        elif choice in (1, 2):
            fileNameToLoad: str = input("Enter the file name for loading: ")
            fileNameToSave: str = input("Enter the file name for saving: ")
            key: int = int(input("Enter the key: "))

            text: str = open(fileNameToLoad).read()
            if choice == 1:
                transformation = encrypt
            else:
                transformation = decrypt
            processed_text: str = process_text(text, transformation, key)
            open(fileNameToSave, 'w').write(processed_text)

            print(f"Processed text: {processed_text}")

if __name__ == '__main__':
    main()
