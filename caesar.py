#implementation of Caesar cipher encryption and decryption

#the function does the encryption and decryption
def encrypt(plaintext:str, key:int)->str:
    return "it is encrypted from " + str(plaintext) + " with key " + int(key)

def decode(plaintext:str, key:int)->str:
    return "it is decrypted from " + str(plaintext) + " with key " + int(key)




def main(plaintext:str, key:int):
    print("Welcome to Caesar cipher program")
    userChoice = input("if you want to decrypt, type 'd' or encrypt, type 'e':")
    print(userChoice)
    if(userChoice == "e"):
        print(encrypt)
    elif(userChoice == "d"):
        print(decode)
    else:
        print("invalid input")

if __name__ == "__main__":
    main(plaintext="hello", key=3)