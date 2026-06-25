# 🔐 Secure Image Steganography Tool

A Python-based GUI application that securely hides and extracts secret messages or files inside images using Steganography and Encryption.

---

## 📖 Overview

The Secure Image Steganography Tool allows users to:

- Hide secret text messages inside images.
- Hide files inside images.
- Extract hidden messages.
- Extract hidden files.
- Encrypt data before embedding for additional security.
- Use a modern Drag & Drop graphical interface.

The application ensures that sensitive information remains concealed within image files while preserving the visual appearance of the image.

---

## ✨ Features

### 🔒 Message Steganography
- Hide secret text messages inside images.
- Extract hidden messages from encoded images.

### 📎 File Steganography
- Hide files inside images.
- Extract hidden files from encoded images.

### 🔐 Encryption
- Uses Fernet encryption from the Cryptography library.
- Data is encrypted before being embedded.

### 🎨 Modern GUI
- Clean and user-friendly interface.
- Light theme design.
- Drag & Drop image support.
- Browse Image option.
- Browse File option.
- Image preview support.

### 🖼 Supported Formats
- PNG
- BMP
- JPG / JPEG (for preview and selection)

---

# 🛠 Technologies Used

- Python 3
- Tkinter
- TkinterDnD2
- Pillow (PIL)
- Cryptography (Fernet)
- Base64 Encoding

---

# 📂 Project Structure

```text
Secure-Image-Steganography-Tool/
│
├── main.py
├── gui.py
├── encryption.py
├── steganography.py
├── requirements.txt
├── README.md
│
└── images/
```

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/JaySolanki108/Secure-Image-Steganography-Tool.git
cd Secure-Image-Steganography-Tool
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 3. Activate Virtual Environment

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

```bash
python3 main.py
```

---

# 🔒 Hide a Secret Message

1. Launch the application.
2. Drag & Drop or Browse an image.
3. Click **Hide Message**.
4. Enter the secret message.
5. Select a save location.
6. Encoded image is generated successfully.

---

# 🔓 Reveal a Secret Message

1. Open the application.
2. Select the encoded image.
3. Click **Reveal Message**.
4. The hidden message will be displayed.

---

# 📎 Hide a File Inside an Image

1. Select an image.
2. Click **Hide File**.
3. Choose the file to hide.
4. Select output image location.
5. File is securely embedded inside the image.

---

# 📂 Extract a Hidden File

1. Select the encoded image.
2. Click **Extract File**.
3. Choose a save location.
4. Hidden file is recovered successfully.

---

# 🖼 GUI Features

The application provides:

- Drag & Drop Area
- Browse Image
- Browse File
- Image Preview
- Hide Message Button
- Reveal Message Button
- Hide File Button
- Extract File Button
- Clear Selection Button

---

# 🔐 Security

The application encrypts all hidden data using Fernet Encryption before embedding it into the image.

Benefits include:

- Confidentiality
- Secure Storage
- Data Protection
- Enhanced Privacy

---

# 📋 Requirements

```txt
cffi==2.0.0
cryptography==49.0.0
pillow==12.2.0
pycparser==3.0
tkinterdnd2
```

---

# 🎯 Project Objective

To develop a secure steganography tool capable of hiding text messages and files inside image files while maintaining image quality and ensuring data confidentiality through encryption.

---

# 🚀 Future Enhancements

- Password-protected extraction
- Multiple file embedding
- Dark Mode UI
- Image capacity indicator
- Audio and Video steganography support
- Cloud storage integration

---

# 📸 Sample Workflow

```text
Original Image
      ↓
Encrypt Data
      ↓
Embed Data into Image
      ↓
Generate Encoded Image
      ↓
Extract Data
      ↓
Decrypt Data
      ↓
Recover Original Message/File
```

---

