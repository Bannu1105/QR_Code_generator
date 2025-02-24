### app.py

from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    if not url:
        return "Invalid URL", 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white').convert('RGB')

    # Load the logo
    logo_path = "static/logo.png"  # Ensure this file exists
    try:
        logo = Image.open(logo_path)
        # Resize the logo to fit in the QR code
        logo_size = (img.size[0] // 5, img.size[1] // 5)  # Adjusted size for better appearance
        logo = logo.resize(logo_size, Image.ANTIALIAS)

        # Calculate position
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
    except FileNotFoundError:
        pass  # If no logo is found, just return the QR code without a logo

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
