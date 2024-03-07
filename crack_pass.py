import hashlib
from tqdm import tqdm 


def convert_text_to_sha1(password):
    hash = hashlib.sha1(password.encode()).hexdigest()
    
    return hash

def main():
    try:
        while True:   
            user_sha1 = input("Enter the Hash SHA1 : ")
            clean_sha1 = user_sha1.strip().lower()

            found = False  

            with open('./rockyou.txt',encoding='utf-8') as f:
                for line in f:
                    password = line.strip()
                    convert_sha1 = convert_text_to_sha1(password)
                    if clean_sha1 == convert_sha1:
                        print(f"Password Found : {password}")
                        found = True
                        break  
            if not found:
                print(f"Password : {user_sha1} Not Found ")

    except KeyboardInterrupt:
        print("\nCancel")


if __name__ == '__main__':
    main()
    


    
    
    
    
    
    
    


    
    
    
    
    
    