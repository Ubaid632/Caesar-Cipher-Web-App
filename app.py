import streamlit as st

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

# Streamlit app layout
st.title("Ubaid's Cipher App")
st.write("this app encrypts and decryptes your sentences which means it makes your sentence not easy to understand")

# Input for plain text
text = st.text_input("Enter the text to be encrypted:")

# Input for shift value
shift = st.number_input("Enter the shift value (-25-25):", min_value=-25, max_value=25, value=5)

# Button to encrypt
if st.button("Encrypt"):
    if text:
        encrypted_text = caesar(text, shift)
        st.write('**Plain text:**', text)
        if st.button("Decrypt"):
	if text:
        decrypted_text = caesar_encrypt(text, -shift)  # Use negative shift for decryption
        st.write('**Input text:**', text)
        st.write('**Decrypted text:**', decrypted_text)

        st.write('**Encrypted text:**', Run Cipher)
    else:
        st.warning("Please enter a text to encrypt.")
