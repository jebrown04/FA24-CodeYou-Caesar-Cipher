# add your code here
def caesar_cipher(text, shift=5):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += encrypted_char
        else:
            
            encrypted_text += char
            
    return encrypted_text

input_message=input("Enter a message:")
encrypted_text = caesar_cipher(input_message, 5)
print(input_message)
print(encrypted_text)
