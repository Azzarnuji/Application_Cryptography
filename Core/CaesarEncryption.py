class CaesarEncryption:
    def caesar_encrypt(self, text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord("A") if char.isupper() else ord("a")
                encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text
    def caesar_decrypt(self, encrypted_text, shift):
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                ascii_offset = ord("A") if char.isupper() else ord("a")
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text
            
    
    
if __name__ == "__main__":
    print(__name__)
    exit("No Direct Access Allowed")