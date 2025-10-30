
import sys
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction == 'encode' or direction == 'decode':
    pass
else:
    print('unknown direction')
    sys.exit(1)
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text,shift_amount):
    encrypted_text = ""
    for char in original_text:
        ascii = ord(char)
        if ascii < 97 or ascii > 122:
            encrypted_text+=chr(ascii)
            continue
        new_ascii = 97 + ((ascii - 97 + shift_amount) % 26)
        encrypted_text += chr(new_ascii)

    return encrypted_text

def decrypt(encrypted_text,original_shift):
    decrypted_text = ""
    for char in encrypted_text:
        ascii = ord(char)
        if ascii < 97 or ascii > 122:
            decrypted_text += chr(ascii)
            continue
        new_ascii = 97 + (((ascii - 97 - shift) % 26 + 26) % 26);
        decrypted_text+=chr(new_ascii)
    return decrypted_text
if direction=='encode':
    encrypted_text = encrypt(text,shift)
    print('encrypted text is: ',encrypted_text)
else:
    decrypted_text = decrypt(text,shift)
    print('decrypted text is: ',decrypted_text)


