def caesar_cipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position + shift_amount) % 26
                cipher_text += alphabet[new_position]
            else:
                cipher_text += letter
        print(f"Here's the encoded result: {cipher_text}")

    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for letter in cipher_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position - shift_amount) % 26
                plain_text += alphabet[new_position]
            else:
                plain_text += letter
        print(f"Here's the decoded result: {plain_text}")

    if direction == 'encode':
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == 'decode':
        decrypt(cipher_text=text, shift_amount=shift)
    else:
        print("Invalid direction. Please type 'encode' or 'decode'.")

caesar_cipher()
        

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = " "

    for letter in original_text:

        if encode_or_decode == decode:
            shift_amount *= -1

        shifted_position = alphabet.index(letter) +v  shift_amount
        shifted_position = shifted_position % len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the encoded result:{output_text}")











# def decrypt(cipher_text, shift_amount):D










