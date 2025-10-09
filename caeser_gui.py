import tkinter as tk
from tkinter import messagebox


# implementation of Caesar cipher encryption and decryption

# the function does the encryption
def encrypt(plaintext:str, key:int)->str:
    result = ""
    for char in plaintext:
        if char.isalpha():
            # handle lowercase and uppercase letters
            start = ord("A") if char.isupper() else ord("a")
            # perform the shift
            result += chr((ord(char) - start + key) % 26 + start)
        else:
            # non-alphabetic characters stay unchanged
            result += char
        return result

# the function does the decryption
def decrypted(ciphertext:str, key:int)->str:
    result = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            # shift backwards
            result += chr((ord(char) - start - key) % 26 + start)
        else:
            result += char
        return result
    

# GUI implementation

def gui_main():
    def on_encrypt():
        text = text_entry.get("1.0", tk.END).strip()
        key_value = key_entry.get()

        if not text:
            messagebox.showwarning("Input Error", "Please enter text to encrypt.")
            return
        if not key_value.isdigit():
            messagebox.showwarning("Input Error", "Key must be a number.")
            return
        

        key = int(key_value)
        encrypted_text = encrypt(text, key)
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, encrypted_text)


    def on_decrypt():
        text = text_entry.get("1.0", tk.END).strip()
        key_value = key_entry.get()

        if not text:
            messagebox.showwarning("Input Error", "Please enter text to decrypt.")
            return
        if not key_value.isdigit():
            messagebox.showwarning("Input Error", "Key must be a number.")
            return

        key = int(key_value)
        decrypted_text = decrypted(text, key)
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, decrypted_text)

# window setup

    root = tk.Tk()
    root.title("Caesar Cipher Encoder / Decoder")
    root.geometry("600x400")
    root.configure(bg="#1e1e1e")

# title table

    tk.Label(root, text="Caesar Cipher Program", font=("Arial", 16, "bold"),
             fg="white", bg="#1e1e1e").pack(pady=10)
    
# text label and box

    tk.Label(root, text="Enter your text:", fg="white", bg="#1e1e1e").pack(anchor="w", padx=15)
    text_entry = tk.Text(root, height=5, width=70, bg="#2e2e2e", fg="white", insertbackground="white")
    text_entry.pack(padx=15, pady=5)

# key entry

    tk.Label(root, text="Enter key (number):", fg="white", bg="#1e1e1e").pack(anchor="w", padx=15)
    key_entry = tk.Entry(root,width=10, bg="#2e2e2e", fg="white", insertbackground="white")
    key_entry.pack(padx=15, pady=5)

# buttons

    button_frame = tk.Frame(root, bg="#1e1e1e")
    button_frame.pack(pady=10)
    tk.Button(button_frame, text="Encrypt", command=on_encrypt, bg="#0078D4", fg="white", width=12).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Decrypt", command=on_decrypt, bg="#107C10", fg="white", width=12).grid(row=0, column=1, padx=10)

# result box

    # result box
    tk.Label(root, text="Result:", fg="white", bg="#1e1e1e").pack(anchor="w", padx=15)
    result_box = tk.Text(root, height=6, width=70, bg="#2e2e2e", fg="lime", insertbackground="white")
    result_box.pack(padx=15, pady=5)

    root.mainloop()

# console fallback (optional)

def main(plaintext:str, key:int):
    print("Welcome to Caesar cipher program")
    userChoice = input("if you want to decrypt, type 'd' or encrypt, type 'e':").lower()
    
    if(userChoice == "e"):
        encrypted = encrypt(plaintext, key)
        print(f"Encrypted text: {encrypted}")

    elif(userChoice == "d"):
        ciphertext = input("Enter the text to decrypt: ")
        print(f"Decrypted text: {decrypted}")


    else:
        print("invalid input")

if __name__ == "__main__":
    # start GUI instead of console
    gui_main()