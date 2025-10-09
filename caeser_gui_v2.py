import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter  # Pillow for image & blur


# Caesar cipher encryption and decryption
def encrypt(plaintext: str, key: int) -> str:
    result = ""
    for char in plaintext:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + key) % 26 + start)
        else:
            result += char
    return result


def decrypted(ciphertext: str, key: int) -> str:
    result = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start - key) % 26 + start)
        else:
            result += char
    return result


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
    root.geometry("1536x864")
    root.resizable(False, False)

    # background image with blur
    bg_image = Image.open(r"C:\Users\IT-User\Desktop\python\python\background.jpg")
    bg_image = bg_image.resize((1536, 864))
    blurred_bg = bg_image.filter(ImageFilter.GaussianBlur(5))  # blur radius
    bg_photo = ImageTk.PhotoImage(blurred_bg)

    # canvas with background
    canvas = tk.Canvas(root, width=1536, height=864, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # halftransparent box in the middle
    box_width, box_height = 700, 400  # slightly larger for readability
    x0 = (1536 - box_width) // 2
    y0 = (864 - box_height) // 2
    box = Image.new("RGBA", (box_width, box_height), (0, 0, 0, 160))  # alpha 160 = semi-transparent
    box_photo = ImageTk.PhotoImage(box)
    canvas.create_image(x0, y0, image=box_photo, anchor="nw")

    # frame over the transparent box
    frame = tk.Frame(root, bg="#000000", highlightthickness=0)
    frame.place(x=x0 + 15, y=y0 + 15, width=box_width - 30, height=box_height - 30)

    # GUI Elements
    tk.Label(frame, text="Caesar Cipher Program", font=("Arial", 20, "bold"),
             fg="white", bg="#000000").pack(pady=15)

    tk.Label(frame, text="Enter your text:", fg="white", bg="#000000", font=("Arial", 12)).pack(anchor="w", padx=20)
    text_entry = tk.Text(frame, height=5, width=70, bg="#2e2e2e", fg="white", insertbackground="white")
    text_entry.pack(padx=20, pady=5)

    tk.Label(frame, text="Enter key (number):", fg="white", bg="#000000", font=("Arial", 12)).pack(anchor="w", padx=20)
    key_entry = tk.Entry(frame, width=10, bg="#2e2e2e", fg="white", insertbackground="white", font=("Arial", 12))
    key_entry.pack(padx=20, pady=5)

    # Buttons (red + white)
    def on_enter(e):
        e.widget.config(bg="#FF5C5C")  # brighter on hover

    def on_leave(e):
        e.widget.config(bg="#CC0000")  # darker again

    button_frame = tk.Frame(frame, bg="#000000")
    button_frame.pack(pady=10)

    encrypt_button = tk.Button(button_frame, text="Encrypt", command=on_encrypt,
                               bg="#CC0000", fg="white", width=15, font=("Arial", 12, "bold"),
                               activebackground="#FF5C5C", activeforeground="white", relief="flat", bd=0)
    encrypt_button.grid(row=0, column=0, padx=15)

    decrypt_button = tk.Button(button_frame, text="Decrypt", command=on_decrypt,
                               bg="#CC0000", fg="white", width=15, font=("Arial", 12, "bold"),
                               activebackground="#FF5C5C", activeforeground="white", relief="flat", bd=0)
    decrypt_button.grid(row=0, column=1, padx=15)

    # hover effects
    encrypt_button.bind("<Enter>", on_enter)
    encrypt_button.bind("<Leave>", on_leave)
    decrypt_button.bind("<Enter>", on_enter)
    decrypt_button.bind("<Leave>", on_leave)

    # output box
    tk.Label(frame, text="Result:", fg="white", bg="#000000", font=("Arial", 12)).pack(anchor="w", padx=20)
    result_box = tk.Text(frame, height=4, width=70, bg="#2e2e2e", fg="lime", insertbackground="white")
    result_box.pack(padx=20, pady=5)

    root.mainloop()


if __name__ == "__main__":
    gui_main()
