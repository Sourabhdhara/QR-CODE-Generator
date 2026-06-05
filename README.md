<div align="center">

# 🚀 QR-CODE-Generator
*A versatile, multi-platform tool for generating beautiful, customized QR codes instantly.*

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/HTML5-Web-E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](index.html)
[![Windows](https://img.shields.io/badge/Windows-Executable-0078D6.svg?style=for-the-badge&logo=windows&logoColor=white)](exe%20file/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE/LICENSE.txt)

<br/>
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg" alt="QR Code Example" width="150" height="150"/>
<br/>

**[🌐 Open Web Version](index.html)** • **[💻 Download Desktop App](#-3-desktop-executables-windows)** • **[🐍 Run Python Script](#-2-python-script)**

</div>

<hr/>

## ✨ Features
- 🎨 **Customizable:** Change foreground and background colors to match your style.
- 📏 **Adjustable Dimensions:** Tweak box and border sizes for perfect scanning.
- 💻 **Cross-Platform:** Available as a lightweight web app, a Windows executable, and raw Python scripts.
- 💾 **Instant Save:** Generate and download your QR codes instantly in high-quality formats (PNG).
- ⚡ **Offline Capable:** Desktop and Python versions run entirely offline.

---

## 🛠️ Choose Your Platform

### 🌐 1. Web Version (HTML/JS)
The easiest way to get started! Run it directly in your browser with zero installation.
1. Simply open the [`index.html`](index.html) file in any modern web browser.
2. Enter your data, customize the colors, and hit **Generate QR**.
3. Click **Download PNG** to save your customized QR code locally.

### 🐍 2. Python Script
For developers who love the terminal or want to integrate this functionality into their own Python projects.

**Prerequisites:**
```bash
pip install qrcode[pil]
```

**Running the Script:**
Navigate to the `python file` directory and run either version:
```bash
cd "python file"
python v2.py
```

**Quick Integration Example:**
```python
import qrcode

# Provide the data to encode
data = "https://github.com"

# Generate the QR Code
img = qrcode.make(data)

# Save the image
img.save("my_awesome_qr.png")
```

### 🪟 3. Desktop Executables (Windows)
Don't want to install Python? We've got you covered with standalone Windows executables.
1. Navigate to the [`exe file/`](exe%20file/) directory.
2. Run `v1.exe` or `v2.exe`.
3. Enjoy an easy-to-use, native desktop interface!

---

## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork** the Project
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

## 📄 License
This project is distributed under the MIT License. See the [`LICENSE.txt`](LICENSE/LICENSE.txt) file for more information.

<div align="center">
  <br/>
  <sub>Built with ❤️ for the open-source community.</sub>
</div>
