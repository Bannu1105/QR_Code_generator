Working of the QR Code Generator
User Input: The user enters a URL or text in the input field.
QR Code Generation: When the "Generate QR Code" button is clicked, the input is sent to the Flask backend.
Processing in Flask:
The backend uses the qrcode library to create a QR code.
A logo can optionally be added at the center of the QR code.
The generated QR code is converted into an image format.
Displaying the QR Code: The generated QR code is sent back to the frontend and displayed.
Download Option: Users can download the QR code as an image.
Technologies Used
Flask: Backend framework for handling requests and processing QR codes.
qrcode (Python library): Used to generate QR codes.
Pillow (PIL): Handles image processing, including adding logos to QR codes.
HTML, CSS, JavaScript: Used for designing the user interface.
Bootstrap (Optional): For styling buttons and layout.
Google Fonts (Poppins): Enhances the text appearance.
