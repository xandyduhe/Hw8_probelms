# Week 3
# problem 
# encrypts and decrypts a message using the caesar cipher with a given key
#
# Xandy Duhe 

def caesar_encrypt(key, message):
    """
    encrypt a message using a caesar cipher with a given key
    """
    # create a list to hold the encrypted characters
    encrypted_message = []
    # iterate through each character in the message
    for char in message:
        if char.isalpha():  # check if character is an alphabet
            # determine the offset based on whether the character is lowercase or uppercase
            offset = ord('A') if char.isupper() else ord('a')
            # shift the character within the bounds of the alphabet and append to the list
            encrypted_message.append(chr((ord(char) - offset + key) % 26 + offset))
        else:
            # non-alphabet characters remain the same
            encrypted_message.append(char)
    # join the list into a single string and return it
    return ''.join(encrypted_message)

def caesar_decrypt(key, message):
    """
    decrypt a message using a caesar cipher with a given key
    """
    # create a list to hold the decrypted characters
    decrypted_message = []
    # iterate through each character in the message
    for char in message:
        if char.isalpha():  # check if the character is an alphabet
            # determine the offset based on whether the character is lowercase or uppercase
            offset = ord('A') if char.isupper() else ord('a')
            # shift the character back within the bounds of the alphabet and append to the list
            decrypted_message.append(chr((ord(char) - offset - key) % 26 + offset))
        else:
            # non-alphabet characters remain the same
            decrypted_message.append(char)
    # join the list into a single string and return it
    return ''.join(decrypted_message)

# example using the quote from julius caesar with a key of 12
original_text = "Experience is the teacher of all things."
key = 12

# encrypt the message
encrypted_text = caesar_encrypt(key, original_text)
print("encrypted:", encrypted_text)

# decrypt the message
decrypted_text = caesar_decrypt(key, encrypted_text)
print("decrypted:", decrypted_text)
