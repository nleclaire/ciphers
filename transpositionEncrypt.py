def main():
    myMessage = 'Common sense is not so common.'
    myKey = 10

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '')

def encryptMessage(key, message):
    # Each string in ciphertext represents a column
    ciphertext = [''] * key

    # Loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column

        # Loop until currentIndex goes past message length
        while currentIndex < len(message):
            # Place character at currentIndex in message at the end of current column in ciphertext list
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over:
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it
    print(ciphertext)
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()