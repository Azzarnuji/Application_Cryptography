from Core.CaesarEncryption import *
class Main:
    def mainMenu(self):
        appCaesarEncryption = CaesarEncryption()
        menu = """ 
            Main Menu Aplikasi
            \n
            1. Encrypt Caesar
            2. Decrypt Caesar
            3. Exit
            """
        print(menu)
        userInput = input("Masukkan Nomor Menu: ")
        if int(userInput) == 1:
            userTxt = input("Masukkan Text Yang Ingin Di Encrypt : ")
            userShift = input('Masukkan Pergeseran Text : ')
            resultEncrypted = appCaesarEncryption.caesar_encrypt(text=userTxt, shift=int(userShift))
            print(f"Hasil Encrypt : {resultEncrypted}")
        elif int(userInput) == 2:
            userTxtDecrypt = input("Masukkan Text Yang Ingin Di Decrypt : ")
            userShift = input('Masukkan Pergeseran Text : ')
            resultDecrypted = appCaesarEncryption.caesar_decrypt(encrypted_text=userTxtDecrypt, shift=int(userShift))
            print(f"Hasil Decrypt : {resultDecrypted} \n")
        elif int(userInput) == 3:
            exit("Thanks For Use")
        else:
            print(f"Menu Dengan Nomor {userInput} Tidak Tersedia")
        

App = Main()
App.mainMenu()