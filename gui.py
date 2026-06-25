import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
from encryption import encrypt_message, decrypt_message
from steganography import encode_image, decode_image
from tkinter import simpledialog
from PIL import Image, ImageTk
import base64

class SteganographyGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Secure Image & File Steganography Tool")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.root.configure(bg="#F4F6F9")
        self.root.resizable(True, True)

        self.image_path = ""
        self.file_path = ""

        self.create_widgets()

    def drop_file(self, event):

        dropped_path = event.data.strip("{}")

        extension = os.path.splitext(
            dropped_path
        )[1].lower()

        image_extensions = [
            ".png",
            ".jpg",
            ".jpeg",
            ".bmp"
        ]

        if extension in image_extensions:

            self.image_path = dropped_path
            img = Image.open(self.image_path)
            img.thumbnail((300, 300))

            photo = ImageTk.PhotoImage(img)

            if hasattr(self, "preview_label"):
                self.preview_label.destroy()

            self.preview_label = tk.Label(
                self.frame,
                image=photo,
                bg="#FFFFFF"
            )

            self.preview_label.image = photo
            self.preview_label.pack(pady=10)
            
            filename = os.path.basename(
                self.image_path
            )

            self.path_label.config(
                text=f"🖼️ Image: {filename}",
                fg="#16A34A",
                font=("Segoe UI", 11, "bold")
            )

        else:

            self.file_path = dropped_path

            filename = os.path.basename(
                self.file_path
            )

            self.path_label.config(
                text=f"📄 File: {filename}",
                fg="#2563EB",
                font=("Segoe UI", 11, "bold")
            )


    def create_widgets(self):

        self.root.configure(bg="#F8FAFC")

        title = tk.Label(
            self.root,
            text="🔐 Secure Image Steganography",
            font=("Segoe UI", 26, "bold"),
            bg="#F8FAFC",
            fg="#0F172A"
        )
        title.pack(pady=20)

        subtitle = tk.Label(
            self.root,
            text="Hide and Extract Secret Messages and Files Inside Images Securely",
            font=("Segoe UI", 11),
            bg="#F8FAFC",
            fg="#64748B"
        )

        subtitle.pack(pady=(0, 20))

        self.frame = tk.Frame(
            self.root,
                bg="#FFFFFF",
                padx=30,
                pady=30
        )
        self.frame.pack(
            padx=40,
            pady=20,
            fill="both",
            expand=True
        )

        self.drop_area = tk.Frame(
            self.frame,
            bg="#FFFFFF",
            bd=0,
            highlightbackground="#CBD5E1",
            highlightthickness=2,
            width=850,
            height=280
        )

        self.drop_area.pack(pady=20)
        self.drop_area.pack_propagate(False)
        self.drop_area.bind(
            "<Enter>",
            lambda e: self.drop_area.config(
                highlightbackground="#2563EB"
            )
        )

        self.drop_area.bind(
            "<Leave>",
            lambda e: self.drop_area.config(
                highlightbackground="#CBD5E1"
            )
        )
        self.drop_area.drop_target_register(DND_FILES)

        self.drop_area.dnd_bind("<<Drop>>", self.drop_file)


        def clear_all(self):

            self.image_path = ""
            self.file_path = ""

            self.path_label.config(
                text="No image selected",
                fg="#64748B",
                font=("Segoe UI", 10)
            )

            if hasattr(self, "preview_label"):
                self.preview_label.destroy()

            self.drag_text.config(
                text="Drag & Drop Image or File Here",
                fg="#0F172A",
                bg="#FFFFFF"
            )


        def drag_enter(event):

            self.drop_area.config(
                bg="#DBEAFE",
                highlightbackground="#2563EB",
                highlightthickness=4
            )

            self.drag_text.config(
                text="📥 Release to Upload Image or File",
                fg="#2563EB",
                bg="#DBEAFE"
            )

        def drag_leave(event):

            self.drop_area.config(
                bg="#FFFFFF",
                highlightbackground="#CBD5E1",
                highlightthickness=2
            )

            self.drag_text.config(
                text="Drag & Drop Image Here",
                fg="#0F172A",
                bg="#FFFFFF"
            )

        self.drop_area.dnd_bind("<<DragEnter>>", drag_enter)
        self.drop_area.dnd_bind("<<DragLeave>>", drag_leave)

        tk.Label(
            self.drop_area,
            text="📂",
            font=("Segoe UI", 50),
            bg="#FFFFFF"
        ).pack(pady=(25, 5))


        self.drag_text = tk.Label(
            self.drop_area,
            text="Drag & Drop Image Here",
            font=("Segoe UI", 18, "bold"),
            bg="#FFFFFF",
            fg="#0F172A"
        )

        self.drag_text.pack()

        browse_link = tk.Label(
            self.drop_area,
            text="Browse Image",
            font=("Segoe UI", 13, "bold underline"),
            fg="#2563EB",
            bg="#FFFFFF",
            cursor="hand2"
        )

        browse_link.pack(pady=(10, 5))

        browse_link.bind(
            "<Button-1>",
            lambda e: self.select_image()
        )

        browse_file = tk.Label(
            self.drop_area,
            text="Browse File",
            font=("Segoe UI", 13, "bold underline"),
            fg="#2563EB",
            bg="#FFFFFF",
            cursor="hand2"
        )

        browse_file.pack()

        browse_file.bind(
            "<Button-1>",
            lambda e: self.select_file()
        )

        self.path_label = tk.Label(
            self.frame,
            text="No image selected",
            bg="#FFFFFF",
            fg="#64748B",
            font=("Segoe UI", 10)
        )
        self.path_label.pack(pady=10)
        
        button_style = {
            "font": ("Segoe UI", 12, "bold"),
            "bg": "#2563EB",
            "fg": "white",
            "activebackground": "#1D4ED8",
            "activeforeground": "white",
            "width": 18,
            "height": 2,
            "bd": 0,
            "cursor": "hand2"
        }

        button_frame = tk.Frame(self.frame, bg="#FFFFFF")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="🔒 Hide Message",
            command=self.encode_message,
            **button_style
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="🔓 Reveal Message",
            command=self.decode_message,
            **button_style
        ).grid(row=0, column=1, padx=10)
        

        tk.Button(
            button_frame,
            text="📎 Hide File",
            command=self.hide_file,
            **button_style
        ).grid(row=0, column=2, padx=10)

        tk.Button(
            button_frame,
            text="📂 Extract File",
            command=self.extract_file,
            **button_style
        ).grid(row=0, column=3, padx=10)

        tk.Button(
            button_frame,
            text="🗑 Clear",
            command=lambda: self.path_label.config(
                text="No image selected",
                fg="#64748B",
                font=("Segoe UI", 10)
            ),
            **button_style
        ).grid(row=0, column=4, padx=10)

    def hide_file(self):

        if not self.image_path:
            messagebox.showerror(
                "Error",
                "Select an image first."
            )
            return

        self.file_path = filedialog.askopenfilename()

        if not self.file_path:
            return

        try:

            with open(self.file_path, "rb") as file:
                file_data = file.read()

            encoded_data = base64.b64encode(
                file_data
            ).decode()

            encrypted = encrypt_message(
                encoded_data
            )

            output_path = filedialog.asksaveasfilename(
                defaultextension=".png"
            )

            if output_path:

                encode_image(
                    self.image_path,
                    encrypted,
                    output_path
                )

                messagebox.showinfo(
                    "Success",
                    "File hidden successfully!"
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def select_image(self):

        self.image_path = filedialog.askopenfilename(
            initialdir=os.path.expanduser("~"),
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
                ("All Files", "*.*")
            ]
        )

        if self.image_path:

            filename = os.path.basename(self.image_path)

            self.path_label.config(
                text=f"📄 File Selected: {filename}",
                fg="#2563EB",
                font=("Segoe UI", 11, "bold")
            )

            img = Image.open(self.image_path)
            img.thumbnail((300, 300))

            photo = ImageTk.PhotoImage(img)

            if hasattr(self, "preview_label"):
                self.preview_label.destroy()

            self.preview_label = tk.Label(
                self.frame,
                image=photo,
                bg="#FFFFFF"
            )

            self.preview_label.image = photo
            self.preview_label.pack(pady=10)
        img.thumbnail((300, 300))

        photo = ImageTk.PhotoImage(img)

        if hasattr(self, "preview_label"):
            self.preview_label.destroy()

        self.preview_label = tk.Label(
            self.frame,
            image=photo,
            bg="#FFFFFF"
        )
        self.preview_label.image = photo
        self.preview_label.pack(pady=10)

    def select_file(self):

        self.file_path = filedialog.askopenfilename(
            filetypes=[
                ("Documents", "*.txt *.pdf *.docx"),
                ("All Files", "*.*")
            ]
        )

        if self.file_path:

            filename = os.path.basename(
                self.file_path
            )

            self.path_label.config(
                text=f"📄 {filename}",
                fg="#2563EB",
                font=("Segoe UI", 11, "bold")
            )
            
    def encode_message(self):

        if not self.image_path:
            messagebox.showerror(
                "Error",
                "Please select an image first."
            )
            return

        message = simpledialog.askstring(
            "Secret Message",
            "Enter the secret message to hide:"
        )

        if not message:
            return

        try:
            encrypted = encrypt_message(message)

            output_path = filedialog.asksaveasfilename(
                initialfile="encoded_image.png",
                defaultextension=".png",
                filetypes=[
                    ("PNG Image", "*.png"),
                    ("BMP Image", "*.bmp")
                ]
            )

            if output_path:

                encode_image(
                    self.image_path,
                    encrypted,
                    output_path
                )

                messagebox.showinfo(
                    "Success",
                    "Message encoded successfully!"
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def decode_message(self):

        if not self.image_path:
            messagebox.showerror(
                "Error",
                "Please select encoded image first."
            )
            return

        try:

            encrypted_data = decode_image(
                self.image_path
            )

            message = decrypt_message(
                encrypted_data
            )

            messagebox.showinfo(
                "Decoded Message",
                message
            )

        except Exception:

            messagebox.showerror(
                "Error",
                "No valid hidden message found."
            )

    def extract_file(self):

        if not self.image_path:
            messagebox.showerror(
                "Error",
                "Select encoded image first."
            )
            return

        try:

            encrypted_data = decode_image(
                self.image_path
            )

            decoded_data = decrypt_message(
                encrypted_data
            )

            binary_data = base64.b64decode(
                decoded_data
            )

            save_path = filedialog.asksaveasfilename(
                initialfile="extracted_file",
                title="Save Extracted File"
            )

            if save_path:

                with open(save_path, "wb") as file:
                    file.write(binary_data)

                messagebox.showinfo(
                    "Success",
                    "File extracted successfully!"
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

def run():
    root = TkinterDnD.Tk()
    SteganographyGUI(root)
    root.mainloop()
