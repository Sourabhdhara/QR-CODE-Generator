import qrcode
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from io import BytesIO

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Set application icon (using a placeholder)
        try:
            self.root.iconbitmap("qr_generator.ico")
        except:
            pass
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header with icon
        header_frame = tk.Frame(self.root, bg="#2c3e50")
        header_frame.pack(pady=(20, 10))
        
        # QR code icon (using a label with QR symbol)
        icon_label = tk.Label(header_frame, text="⎗", font=("Segoe UI", 32), 
                             bg="#2c3e50", fg="#3498db")
        icon_label.pack()
        
        title = tk.Label(header_frame, text="QR Code Generator", 
                        font=("Segoe UI", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
        title.pack(pady=(10, 0))
        
        subtitle = tk.Label(header_frame, text="Create custom QR codes instantly", 
                           font=("Segoe UI", 10), bg="#2c3e50", fg="#bdc3c7")
        subtitle.pack()
        
        # Form frame with modern styling
        form_frame = tk.Frame(self.root, bg="#34495e", padx=20, pady=20, 
                             relief=tk.RAISED, bd=2)
        form_frame.pack(pady=20, padx=40, fill=tk.X)
        
        # Form title
        form_title = tk.Label(form_frame, text="QR Code Settings", 
                             font=("Segoe UI", 12, "bold"), bg="#34495e", fg="#ecf0f1")
        form_title.pack(pady=(0, 15))
        
        # Form fields
        self.entry = self.add_labeled_entry(form_frame, "Data to encode:", "Enter URL or text")
        self.box_size_entry = self.add_labeled_entry(form_frame, "Box size:", "10", width=10)
        self.border_size_entry = self.add_labeled_entry(form_frame, "Border size:", "4", width=10)
        self.fill_color_entry = self.add_labeled_entry(form_frame, "Fill color:", "#3498db", width=15)
        self.bg_color_entry = self.add_labeled_entry(form_frame, "Background color:", "#ffffff", width=15)
        
        # Generate button with modern style
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=10)
        
        self.generate_btn = tk.Button(button_frame, text="Generate QR Code", 
                                     command=self.generate_qr, font=("Segoe UI", 12, "bold"),
                                     bg="#3498db", fg="white", activebackground="#2980b9",
                                     relief=tk.FLAT, padx=20, pady=10, cursor="hand2")
        self.generate_btn.pack()
        
        # QR code display area with frame
        qr_display_frame = tk.Frame(self.root, bg="#34495e", padx=10, pady=10, 
                                   relief=tk.SUNKEN, bd=1)
        qr_display_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)
        
        qr_title = tk.Label(qr_display_frame, text="Your QR Code", 
                           font=("Segoe UI", 10, "bold"), bg="#34495e", fg="#ecf0f1")
        qr_title.pack(pady=(0, 10))
        
        self.qr_label = tk.Label(qr_display_frame, bg="#2c3e50", 
                                text="QR code will appear here", 
                                font=("Segoe UI", 9), fg="#bdc3c7")
        self.qr_label.pack(pady=20, fill=tk.BOTH, expand=True)
        
    def add_labeled_entry(self, parent, label_text, default="", width=25):
        row = tk.Frame(parent, bg="#34495e")
        row.pack(pady=8, fill=tk.X)
        
        tk.Label(row, text=label_text, font=("Segoe UI", 10), 
                bg="#34495e", fg="#ecf0f1", anchor="w", width=15).pack(side=tk.LEFT)
        
        entry = tk.Entry(row, font=("Segoe UI", 10), width=width,
                        relief=tk.FLAT, bg="#ecf0f1", fg="#2c3e50")
        entry.insert(0, default)
        entry.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Add subtle separator
        separator = ttk.Separator(parent, orient='horizontal')
        separator.pack(fill=tk.X, pady=2)
        
        return entry
        
    def generate_qr(self):
        data = self.entry.get()
        
        try:
            box_size = int(self.box_size_entry.get())
            border_size = int(self.border_size_entry.get())
            fill_color = self.fill_color_entry.get()
            bg_color = self.bg_color_entry.get()
        except ValueError:
            messagebox.showerror("Input Error", "Box size and border size must be integers.")
            return

        if not data or data == "Enter URL or text":
            messagebox.showwarning("Input Error", "Please enter some data.")
            return

        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border_size,
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color=fill_color, back_color=bg_color)
            
            # Resize for display
            resized_img = img.resize((250, 250), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(resized_img)
            
            # Update the QR code display
            self.qr_label.config(image=tk_img, text="")
            self.qr_label.image = tk_img

            # Show the image in default viewer
            img.show()

        except Exception as e:
            messagebox.showerror("QR Generation Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()