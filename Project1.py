import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter some text or URL")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img = qr_img.resize((200, 200))
    
    img = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=img)
    qr_label.image = img
    
    save_button.config(state=tk.NORMAL)
    
    global generated_qr
    generated_qr = qr_img

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        generated_qr.save(file_path)
        messagebox.showinfo("Saved", f"QR Code saved successfully at {file_path}")

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")

entry_label = tk.Label(root, text="Enter text or URL:")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

save_button = tk.Button(root, text="Save QR Code", command=save_qr, state=tk.DISABLED)
save_button.pack(pady=10)

root.mainloop()

