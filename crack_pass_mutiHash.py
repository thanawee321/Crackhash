import hashlib
from tqdm import tqdm  
import os
import pyqrcode
import pyperclip



list_password = []



def type_list(menu):
    
    if menu == '1':
        return "-- MD5 HASH --"
    if menu == '2':
        return "-- SHA1 HASH --"
    if menu == '3':
        return "-- SHA256 HASH --"
    if menu == '4':
        return "-- SHA384 HASH --"
    if menu == '5':
        return "-- SHA512 HASH --"



def convert_text_to_md5(text_password):
    
    digest = hashlib.md5(text_password.encode()).hexdigest()
    return digest

def convert_text_to_sha1(text_password):
    
    digest = hashlib.sha1(text_password.encode()).hexdigest()
    return digest

def convert_text_to_sha256(text_password):
    
    digest = hashlib.sha256(text_password.encode()).hexdigest()
    return digest

def convert_text_to_sha384(text_password):
    
    digest = hashlib.sha384(text_password.encode()).hexdigest()
    return digest

def convert_text_to_sha512(text_password):
    
    digest = hashlib.sha512(text_password.encode()).hexdigest()
    return digest



def get_data_password():
    
    file = input("Setup the list file password : ")
    try:
        #with open('rockyou.txt', encoding='utf-8') as f:
        with open(file, encoding='utf-8') as f:
            
            for i in tqdm(f, desc="Loading...", ascii=False, ncols=100):
                list_password.append(i.strip())
                
    except Exception as e:
        print("[-] File not found or Wrong location source!!")
        print(f"[!] {e}\n")
        
    except KeyboardInterrupt:
        print("[+] Exit to Program")
        
    return list_password



def create_hash():
    
    try:
        while True:
            print("-- Create HASH --")
            print("[1] MD5 HASH")
            print("[2] SHA1 HASH")
            print("[3] SHA256 HASH")
            print("[4] SHA384 HASH")
            print("[5] SHA512 HASH")

            you_hash = input("\n[+] Insert you string : ")
            create = input("[+] Select to hash mode : ")
            
            if create == '1':
               pyperclip.copy(convert_text_to_md5(you_hash))
               this_hash = pyperclip.paste()
               print("-------------------------------------------------------")
               print("[+] [Status] -- Generate Sucessfully -- ")
               print(f"[+] This HASH = {this_hash}")
               os.system('pause')
               os.system('cls')
               break
           
            elif create == '2':
                pyperclip.copy(convert_text_to_sha1(you_hash))
                this_hash = pyperclip.paste()
                print("-------------------------------------------------------")
                print("[+] [Status] -- Generate Sucessfully -- ")
                print(f"[+] This HASH = {this_hash}")
                os.system('pause')
                os.system('cls')
                break
            
            elif create == '3':
                pyperclip.copy(convert_text_to_sha256(you_hash))
                this_hash = pyperclip.paste()
                print("-------------------------------------------------------")
                print("[+] [Status] -- Generate Sucessfully -- ")
                print(f"[+] This HASH = {this_hash}")
                os.system('pause')
                os.system('cls')
                break
            
            elif create == '4':
                pyperclip.copy(convert_text_to_sha384(you_hash))
                this_hash = pyperclip.paste()
                print("-------------------------------------------------------")
                print("[+] [Status] -- Generate Sucessfully -- ")
                print(f"[+] This HASH = {this_hash}")
                os.system('pause')
                os.system('cls')
                break
                
            elif create == '5':
                pyperclip.copy(convert_text_to_sha512(you_hash))
                this_hash = pyperclip.paste()
                print("-------------------------------------------------------")
                print("[+] [Status] -- Generate Sucessfully -- ")
                print(f"[+] This HASH = {this_hash}")
                os.system('pause')
                os.system('cls')
                break

            else:
                print("[!] Please Select menu again..")
                break
            
    except KeyboardInterrupt:
        os.system('cls')
        print("\n [!] Back to main menu")
    
    

def advance():
    
    try:
        os.system('cls')
        
        while True:
            print("-- Advance Mode --\n")
            print("[1] Set up the source file password")
            print("[2] Create the Hash\n")        

            menuAD = input("[+] Select menu advance : ")
            if menuAD == '1':
                os.system('cls')
                get_data_password()
                break
            
            elif menuAD == '2':
                os.system('cls')
                create_hash()
                break
            else:
                os.system('cls')
                print("[!] Please select menu again...\n")
                

    except KeyboardInterrupt:
        os.system('cls')
        print("\n [!] Back to main menu")
        
        
        
def main(menu):
    try:
        while True:
            os.system('cls')  
            print(type_list(menu))
            print("*** Do you want to exit menu,Please Ctrl+c for exit ***\n")
            user_hash = input("Enter your hash: ").strip().lower()
            
            for line in list_password:
                
                if menu == '1':
                    convert_hash = convert_text_to_md5(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[+] [Status] -- Password Found -- ")
                        print(f"[+] This is a Password = {line}")
                        os.system('pause')
                        break
                    
                if menu == '2':
                    convert_hash = convert_text_to_sha1(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[+] [Status] -- Password Found -- ")
                        print(f"[+] This is a Password = {line}")
                        os.system('pause')
                        break
                
                if menu == '3':
                    convert_hash = convert_text_to_sha256(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[+] [Status] -- Password Found -- ")
                        print(f"[+] This is a Password = {line}")
                        os.system('pause')
                        break
                
                if menu == '4':
                    convert_hash = convert_text_to_sha384(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[+] [Status] -- Password Found -- ")
                        print(f"[+] This is a Password = {line}") 
                        os.system('pause')
                        break
                    
                if menu == '5':
                    convert_hash = convert_text_to_sha512(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[+] [Status] -- Password Found -- ")
                        print(f"[+] This is a Password = {line}") 
                        os.system('pause')
                        break
                    
            else:
                print("[-] [Status] -- Password NOT Found --")
                print("[!] Please check your hash again")
                os.system('pause')  

    except KeyboardInterrupt:
        os.system('cls')  
        print("[!] Back to Main menu")
        
        
        
def help_menu():
    print("** Help Menu *** ")
    print("Ctrl+C : Exit to menu/Exit to program")
    print("MD5 HASH : is a menu hash decrypt")
    print("SHA1 HASH : is a menu hash decrypt")
    print("SHA256 HASH : is a menu hash decrypt")
    print("SHA384 HASH : is a menu hash decrypt")
    print("SHA512 HASH : is a menu hash decrypt")
    print("Setup source file Password : is a setup source file password,Do you want to change list file password")



if __name__ == '__main__':
    get_data_password() 
    os.system('pause')
    os.system('cls')
    try:
        
        while True:
            print("\n|-- Welcome to Program HASH Convert!!! --|")
            print("           Dev by BabyH@ck V.4.2.7\n")
            print("[1] MD5 HASH")
            print("[2] SHA1 HASH")
            print("[3] SHA256 HASH")
            print("[4] SHA384 HASH")
            print("[5] SHA512 HASH")
            print("\n[99] Advance Mode")
            print("\n*** Do you want to help menu,Please Enter Help ***")
            print("*** Do you want to exit menu,Please Ctrl+c for exit ***")
            print("-----------------------------------------------------------")
            menu = str(input("[+] Select menu : "))
            if menu in ['1', '2', '3', '4', '5','6']:
                os.system('cls')  
                main(menu)  
                
            elif menu == 'help' or menu == 'Help':
                os.system('cls')
                help_menu()
                os.system('pause')
               
            elif menu == '99':
                os.system('cls')
                advance()
                
            else:
                os.system('cls')  
                print("[!] Select menu again")

    except KeyboardInterrupt:
        os.system('cls')
        print("\n[!] Exit the program")
        print("-------------------------------------")
        print("Do you want to Support me? You can sent some donate to me hahaha at a below this message")
        pay = pyqrcode.create(content="I need Hee")
        print(pay.terminal(module_color='white', background='black'))  
        os.system('pause')