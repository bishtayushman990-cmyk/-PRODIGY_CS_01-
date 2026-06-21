import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Caesar Cipher Functions
# ----------------------------

def encrypt(message, shift):
    result = ""

    for char in message:

        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


def decrypt(message, shift):
    result = ""

    for char in message:

        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            result += char

    return result


def brute_force(message):

    output = ""

    for shift in range(26):

        decrypted = ""

        for char in message:

            if char.isupper():
                decrypted += chr(
                    (ord(char) - ord('A') - shift) % 26 + ord('A')
                )

            elif char.islower():
                decrypted += chr(
                    (ord(char) - ord('a') - shift) % 26 + ord('a')
                )

            else:
                decrypted += char

        output += f"Shift {shift}: {decrypted}\n"

    return output


# ----------------------------
# Button Functions
# ----------------------------

def encrypt_text():
    try:
        message = message_entry.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())

        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, encrypt(message, shift))

    except ValueError:
        messagebox.showerror("Error", "Enter a valid shift value")


def decrypt_text():
    try:
        message = message_entry.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())

        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, decrypt(message, shift))

    except ValueError:
        messagebox.showerror("Error", "Enter a valid shift value")


def brute_force_text():

    message = message_entry.get("1.0", tk.END).strip()

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, brute_force(message))


def clear_all():

    message_entry.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    result_box.delete("1.0", tk.END)


# ----------------------------
# GUI
# ----------------------------

root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("700x600")

title = tk.Label(
    root,
    text="CAESAR CIPHER TOOL",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

message_label = tk.Label(root, text="Enter Message")
message_label.pack()

message_entry = tk.Text(root, height=5, width=60)
message_entry.pack(pady=5)

shift_label = tk.Label(root, text="Shift Value")
shift_label.pack()

shift_entry = tk.Entry(root)
shift_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    command=encrypt_text
)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    command=decrypt_text
)
decrypt_btn.grid(row=0, column=1, padx=5)

bruteforce_btn = tk.Button(
    button_frame,
    text="Brute Force",
    command=brute_force_text
)
bruteforce_btn.grid(row=0, column=2, padx=5)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all
)
clear_btn.grid(row=0, column=3, padx=5)

result_label = tk.Label(root, text="Result")
result_label.pack()

result_box = tk.Text(root, height=15, width=80)
result_box.pack(pady=10)

root.mainloop()