def encrypt(rawText: str, key: int) -> str:
    result: str = ''
    for char in rawText:
        if char == '\0':
            break

        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr(((ord(char) - ord(base) + key) % 26) + ord(base))
        else:
            result += chr((ord(char) + key) % 68)
        
    return result

def decrypt(encryptedText: str, key: int) -> str:
    result: str = ''
    for char in encryptedText:
        if char == '\0':
            break

        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr(((ord(char) - ord(base) - key + 26) % 26) + ord(base))
        else:
            result += chr((ord(char) - key) % 68)
        
    return result

def main():
    pass

if __name__ == '__main__':
    main()
