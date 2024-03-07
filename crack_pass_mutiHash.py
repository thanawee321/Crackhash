import hashlib
from tqdm import tqdm  # เรียกใช้ tqdm เพื่อแสดงแถบความคืบหน้า
import os
import pyqrcode

# กำหนดรายการเพื่อเก็บรหัสผ่าน
list_password = []

# กำหนดฟล็อกเพื่อตรวจสอบว่าพบรหัสผ่านหรือไม่

# ฟังก์ชันเพื่อแสดงตัวเลือกรายการเมนูโดยใช้ข้อมูลเมนูเข้ารหัส
def type_list(menu):
    # กำหนดการแมปหมายเลขเมนูเพื่อประเภทการเข้ารหัสแต่ละชนิด
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

# ฟังก์ชันเพื่อแปลงข้อความรหัสผ่านเป็น MD5 hash
def convert_text_to_md5(text_password):
    digest = hashlib.md5(text_password.encode()).hexdigest()
    return digest

# ฟังก์ชันเพื่อแปลงข้อความรหัสผ่านเป็นรหัส hash SHA1
def convert_text_to_sha1(text_password):
    digest = hashlib.sha1(text_password.encode()).hexdigest()
    return digest

# ฟังก์ชันเพื่อแปลงข้อความรหัสผ่านเป็นรหัส hash SHA256
def convert_text_to_sha256(text_password):
    digest = hashlib.sha256(text_password.encode()).hexdigest()
    return digest

# ฟังก์ชันเพื่อแปลงข้อความรหัสผ่านเป็นรหัส hash SHA384
def convert_text_to_sha384(text_password):
    digest = hashlib.sha384(text_password.encode()).hexdigest()
    return digest

# ฟังก์ชันเพื่อแปลงข้อความรหัสผ่านเป็นรหัส hash SHA512
def convert_text_to_sha512(text_password):
    digest = hashlib.sha512(text_password.encode()).hexdigest()
    return digest



# ฟังก์ชันเพื่ออ่านข้อมูลรหัสผ่านจากไฟล์
def get_data_password():
    file = input("Setup the list file password : ")
    try:
        with open(file, encoding='utf-8') as f:
            # ใช้ tqdm เพื่อแสดงแถบความคืบหน้าในขณะอ่านบรรทัดจากไฟล์
            for i in tqdm(f, desc="Loading...", ascii=False, ncols=100):
                list_password.append(i.strip())
    except Exception as e:
        print("[-] File not found or Wrong location source!!")
        print(f"[!] {e}\n")
    except KeyboardInterrupt:
        print("[+] Exit to Program")
    return list_password

# ฟังก์ชันหลักเพื่อทำการเปรียบเทียบรหัสผ่าน
def main(menu):
    try:
        while True:
            os.system('cls')  # เคลียร์หน้าจอ
            print(type_list(menu))
            user_hash = input("Enter your hash: ").strip().lower()

            # ลูปผ่านรายการรหัสผ่าน
            for line in list_password:
                
                # ตรรจสอบเหมือนกันสำหรับชนิดของ hash อื่น ๆ
                # คุณสามารถทำซ้ำบล็อค if ด้านบนสำหรับ SHA1, SHA256, SHA384, SHA512
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
                os.system('pause')  # หยุดการดำเนินการหากรหัสผ่านไม่พบ

    except KeyboardInterrupt:
        os.system('cls')  # เคลียร์หน้าจอ
        print("Back to Main menu")

# ฟังก์ชันเพื่อจัดการการเลือกเมนูและการนำทาง
if __name__ == '__main__':
    get_data_password() # โหลดข้อมูลรหัสผ่านจากไฟล์
    os.system('pause')
    os.system('cls')
    try:
        while True:
            print("\n|-- Welcome to Program HASH Convert!!! --|")
            print("           Dev by BabyH@ck V.3.7.9\n")
            print("[1] MD5 HASH")
            print("[2] SHA1 HASH")
            print("[3] SHA256 HASH")
            print("[4] SHA384 HASH")
            print("[5] SHA512 HASH")
            print("\n[99] Setup source file Password")
            
            print("\n*** Do you want to help menu,Please Enter Help ***")
            print("-------------------------------------------------------")
            menu = str(input("Select menu : "))
            if menu in ['1', '2', '3', '4', '5']:
                os.system('cls')  # เคลียร์หน้าจอ
                main(menu)  # เรียกใช้ฟังก์ชันหลักตามที่เลือกในเมนู
                
            elif menu == 'help' or menu == 'Help':
                os.system('cls')
                print("** Help Menu *** ")
                print("Ctrl+C : Exit to menu/Exit to program")
                print("MD5 HASH : is a menu hash decrypt")
                print("SHA1 HASH : is a menu hash decrypt")
                print("SHA256 HASH : is a menu hash decrypt")
                print("SHA384 HASH : is a menu hash decrypt")
                print("SHA512 HASH : is a menu hash decrypt")
                print("Setup source file Password : is a setup source file password,Do you want to change list file password")
                os.system('pause')
                os.system('cls')
                
            elif menu == '99':
                os.system('cls')
                get_data_password()
            else:
                os.system('cls')  # เคลียร์หน้าจอ
                print("[!] Select menu again")

    except KeyboardInterrupt:
        os.system('cls')
        print("\nExit the program")
        print("-------------------------------------")
        print("Do you want to Support me? You can sent some donate to me hahaha at a below this message")
        pay = pyqrcode.create(content="0991626437")
        print(pay.terminal(module_color='white', background='black'))  
        os.system('pause')



#human version

"""import hashlib
from tqdm import tqdm
import os


list_password = [] 
found = False 

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
    with open('./rockyou.txt', encoding='utf-8') as f: 
        for i in tqdm(f, desc="Loading...", ascii=False, ncols=100):     
            list_password.append(i.strip())
    return list_password



def main(menu):
    
    try:
        while(True):
            os.system('cls')
            
            print(type_list(menu))
            user_hash = input("Enter you hash : ").strip().lower()
            
            for line in list_password:
                
                if menu == '1':
                    convert_hash = convert_text_to_md5(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[Status] -- Password Found -- ")
                        print(f"This is a Password = {line}")
                        os.system('pause')
                        break
                    
                if menu == '2':
                    convert_hash = convert_text_to_sha1(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[Status] -- Password Found -- ")
                        print(f"This is a Password = {line}") 
                        os.system('pause')
                        break
                
                if menu == '3':
                    convert_hash = convert_text_to_sha256(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[Status] -- Password Found -- ")
                        print(f"This is a Password = {line}") 
                        os.system('pause')
                        break
                
                
                if menu == '4':
                    convert_hash = convert_text_to_sha384(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[Status] -- Password Found -- ")
                        print(f"This is a Password = {line}") 
                        os.system('pause')
                        break
                    
                if menu == '5':
                    convert_hash = convert_text_to_sha512(line)
                    if convert_hash == user_hash:
                        print("-------------------------------------------------------")
                        print("[Status] -- Password Found -- ")
                        print(f"This is a Password = {line}") 
                        os.system('pause')
                        break
                
                
            else:
                print("[Status] -- Password NOT Found --")
                print("Please check you hash agian")
                os.system('pause')    
                    
                    
                    
    except KeyboardInterrupt:
        os.system('cls')
        print("Back to Main menu")
    
    
    

if __name__ == '__main__':
    
    get_data_password()
    os.system('cls')
    
   
    try:
       while(True):
        print("-- Welcome to Program HASH Convert!!! --") 
        print("[1] MD5 HASH")
        print("[2] SHA1 HASH")
        print("[3] SHA256 HASH")
        print("[4] SHA384 HASH")
        print("[5] SHA512 HASH")
        
        menu = input("Select menu : ")
        if menu == '1':
            os.system('cls')
            main(menu)
            
        elif menu == '2':
            os.system('cls')
            main(menu)
            
        elif menu == '3':
            os.system('cls')
            main(menu)
            
        elif menu == '4':
            os.system('cls')
            main(menu)
            
        elif menu == '5':
            os.system('cls')
            main(menu)
            
        else:
            os.system('cls')
            print("Select menu agian")
        
    except KeyboardInterrupt:
        print("\nExit to program")"""