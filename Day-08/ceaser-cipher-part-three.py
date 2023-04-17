'''
Ceaser's Cipher Part Three: REORGANISING CODE

Such that the two functions encypt() and decrypt() can be inside the same function; ceaser()
since their code is mostly repetition anyway
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ''
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'decode':
            if shift_amount < 0: # instead of this nested if, Angela simply moved the if cipher direction
                shift_amount *= -1 # if statement out of the for loop to debug the decode issue. Revisit Day 8 if you can't remember
                -shift_amount
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
