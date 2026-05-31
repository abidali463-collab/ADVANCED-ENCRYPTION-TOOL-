import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

with open("key.key", "rb") as file:
    key = file.read()

fernet = Fernet(key)


def encrypt_file():

    filepath = filedialog.askopenfilename()

    if not filepath:
        return

    try:
        with open(filepath, "rb") as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        with open(filepath, "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo(
            "Success",
            "File Encrypted Successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def decrypt_file():

    filepath = filedialog.askopenfilename()

    if not filepath:
        return

    try:
        with open(filepath, "rb") as file:
            data = file.read()

        decrypted_data = fernet.decrypt(data)

        with open(filepath, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo(
            "Success",
            "File Decrypted Successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Advanced Encryption Tool")
root.geometry("500x300")

title = tk.Label(
    root,
    text="Advanced Encryption Tool",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)

encrypt_button = tk.Button(
    root,
    text="Encrypt File",
    width=20,
    height=2,
    command=encrypt_file
)

encrypt_button.pack(pady=10)

decrypt_button = tk.Button(
    root,
    text="Decrypt File",
    width=20,
    height=2,
    command=decrypt_file
)

decrypt_button.pack(pady=10)

exit_button = tk.Button(
    root,
    text="Exit",
    width=20,
    height=2,
    command=root.quit
)

exit_button.pack(pady=10)

root.mainloop()

