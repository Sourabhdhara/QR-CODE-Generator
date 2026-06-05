# QR-CODE-Generator

## Overview
A simple project to generate QR codes using Python. This script allows you to create QR codes for various types of information, such as URLs, text, contact info, and more.

## Features
- Generate QR codes for any text or link
- Save generated QR codes as image files (PNG, JPG, etc.)
- User-friendly and easy to use

## Requirements
- Python >= 3.6
- `qrcode` Python library
- `Pillow` library for image processing

## Installation
pip install qrcode[pil]

## Usage

1. Run the Python script using:
    ```
    python main.py
    ```

2. Enter the data you want to encode as a QR code.

3. The generated QR code image will be saved to your project directory.

### Example
import qrcode

data = "https://example.com"
img = qrcode.make(data)
img.save("example_qr.png")

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

