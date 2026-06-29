print("Welcome to Text Encryptor")
while True:
    Ed = input("press e to encrypt, d to decrypt, or q to quit: ")  
    if Ed == 'e':
        text = input("enter a message to encrypt: ")

        encryptedText = ""

        for char in text:
            ech = chr(ord(char) + 16)
            encryptedText += ech
        print(f"your encrypted message is: {encryptedText}")
    elif Ed == 'd':
        text = input("enter a message to decrypt: ")

        decryptedText = ""

        for char in text:
            dch = chr(ord(char) - 16)
            decryptedText += dch
        print(f"your decrypted message is: {decryptedText}")
    elif Ed == 'q':
        break
    else:
        print('INVALID INPUT\a')
