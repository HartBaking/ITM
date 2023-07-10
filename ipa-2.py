#!/usr/bin/env python
# coding: utf-8

# In[8]:


def shift_letter(letter, shift):
    num_val = ord(letter.upper()) + shift
    if num_val > 90:
        rep_num = num_val - (num_val % 90) + 64
        letter_val1 = chr(rep_num)
        return letter_val1
    elif letter == " ":
        return " "
        
    else :
        letter_val2 = chr(num_val)
        return letter_val2
        

sample_shift = shift_letter("E",382)
print(sample_shift)



def caesar_cipher(message, shift):
    encrypted_caesar = ""

    for char in message:
        if char == " ":
            encrypted_caesar += " "
        else:
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_caesar += shifted_char
    return encrypted_caesar

sample_caesar = caesar_cipher("HELLO WORLD", 5)
print(sample_caesar)




def shift_by_letter(letter, letter_shift):
    if letter == " " or letter_shift == " ":
        return " "
        
    else:
        shift_bylet = ord(letter_shift) - 65 + ord(letter)
        if shift_bylet > 90:
            shift_over = shift_bylet - (shift_bylet % 90) + 64
            sbl_output1 = chr(shift_over)
            return sbl_output1
        else:
            sbl_output = chr(shift_bylet)
        
            return sbl_output

print(shift_by_letter(" ", "A"))
    
        


def vigenere_cipher(message, key):
    encrypted_vig = ""
    key_length = len(key)
    key_repeat = (key * (len(message) // key_length)) + key[:len(message) % key_length]

    for i in range(len(message)):
        char = message[i]
        key_char = key_repeat[i]

        if char.isalpha():
            key_conv = ord(key_char.upper()) - 65
            shift_char = chr((ord(char.upper()) - 65 + key_conv) % 26 + 65)

            

            encrypted_vig += shift_char
        else:
            encrypted_vig += char

    return encrypted_vig

sample_vig = vigenere_cipher("HELLO WORLD", "KEY")
print(sample_vig)




def scytale_cipher(message, shift):
    encrypted_scy = ""
    
    if len(message) % shift != 0:
        underscores_needed = shift - (len(message) % shift)
        
        message += "_" * underscores_needed
        
    
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        encrypted_scy += message[index]
        
    return encrypted_scy
        
print(scytale_cipher("INFORMATION_AGE", 3))



def scytale_decipher(message, shift):
    decrypted_scy = ""

    num_rows = (len(message) - 1) // shift + 1

    for i in range(len(message)):
        index = (i % num_rows) * shift + (i // num_rows)

        decrypted_scy += message[index]

    return decrypted_scy

print(scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8))


# In[ ]:




