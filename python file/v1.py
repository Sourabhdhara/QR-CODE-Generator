import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    try:
        box_size = int(box_size_entry.get())
        border_size = int(border_size_entry.get())
        fill_color = fill_color_entry.get()
        bg_color = bg_color_entry.get()
    except ValueError:
        messagebox.showerror("Input Error", "Box size and border size must be integers.")
        return

    if not data:
        messagebox.showwarning("Input Error", "Please enter some data.")
        return

    try:
        qr = qrcode.QRCode(box_size=box_size, border=border_size)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=bg_color)

        resized_img = img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(resized_img)
        qr_label.config(image=tk_img)
        qr_label.image = tk_img

        img.show()

    except Exception as e:
        messagebox.showerror("QR Generation Error", str(e))

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("460x640")
root.resizable(False, False)
root.configure(bg="#f0f4f7")
root.iconbitmap("qr_generator.ico")

title = tk.Label(root, text="QR Code Generator", font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#333")
title.pack(pady=(20, 10))

form_frame = tk.Frame(root, bg="#f0f4f7")
form_frame.pack(pady=10)

def add_labeled_entry(label_text, default="", width=30):
    row = tk.Frame(form_frame, bg="#f0f4f7")
    row.pack(pady=5)
    tk.Label(row, text=label_text, font=("Segoe UI", 10), bg="#f0f4f7", anchor="w", width=25).pack(side="left")
    entry = tk.Entry(row, font=("Segoe UI", 10), width=width)
    entry.insert(0, default)
    entry.pack(side="right")
    return entry

entry = add_labeled_entry("Enter Data:")
box_size_entry = add_labeled_entry("Box Size (e.g. 10):", "10", 10)
border_size_entry = add_labeled_entry("Border Size (e.g. 1):", "1", 10)
fill_color_entry = add_labeled_entry("Fill Color (e.g. black):", "lightblue", 15)
bg_color_entry = add_labeled_entry("Background Color (e.g. white):", "black", 15)

tk.Button(root, text="Generate QR", command=generate_qr,
          font=("Segoe UI", 12), bg="#4caf50", fg="white",
          activebackground="#45a049", relief="flat", padx=10, pady=5).pack(pady=20)

qr_label = tk.Label(root, bg="#f0f4f7")
qr_label.pack(pady=10)

root.mainloop()