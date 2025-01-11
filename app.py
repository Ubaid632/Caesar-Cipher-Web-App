import streamlit as st

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return caesar_cipher(text, -shift)

# App Title
st.title("Aqsi's Cipher App")  # Customize with your name
st.write("The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted by a certain number of positions in the alphabet.")

# User input
text = st.text_input("Enter the text you want to encrypt/decrypt:")

shift = st.slider("Select Shift Value", min_value=1, max_value=25, value=5)

# Encrypt button
if st.button("Run Cipher"):
    encrypted_text = caesar_cipher(text, shift)
    st.write("Encrypted Text:", encrypted_text)

# Decrypt button
if st.button("Decrypt Now!"):
    decrypted_text = decrypt(text, shift)
    st.write("Decrypted Text:", decrypted_text)

