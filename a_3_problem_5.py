# Week 3
# problem 5
# attempts to crack a caesar cipher by trying all possible shift keys and printing the results
#
# Xandy Duhe 

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
            offset = ord('a') if char.islower() else ord('A')
            # shift the character back within the bounds of the alphabet
            decrypted_message.append(chr((ord(char) - offset - key) % 26 + offset))
        else:
            # non-alphabet characters remain the same
            decrypted_message.append(char)
    # join the list into a single string and return it
    return ''.join(decrypted_message)

# the encrypted message to be decrypted
encrypted_message = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"

# try all possible keys from 0 to 25 and print the results
for key in range(26):
    decrypted_text = caesar_decrypt(key, encrypted_message)
    print(f"key {key}: {decrypted_text}")

