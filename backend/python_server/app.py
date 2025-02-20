from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import imgkit
import os
import sys
import json
import logging
from dotenv import load_dotenv
import qrcode
import base64
import evolis
from io import BytesIO

# Add the evolis library path
sys.path.append(os.path.join(os.path.dirname(__file__), 'evolis'))

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables from .env file
load_dotenv()
API_IP_ADDRESS = os.getenv('API_IP_ADDRESS')

# Printer mapping based on IP
PRINTER_MAP = {
    "192.168.8.50": "Evolis Primacy 2 (LAN)",
    "192.168.8.51": "Evolis Primacy 2 (LAN 2)",
    "192.168.0.50": "Evolis Primacy 2 (PC)"
}

# Font size calculation function
def calculate_font_size(name, max_font_size=24, min_font_size=14, max_length=20):
    length = len(name)
    if length <= max_length:
        return max_font_size
    scaling_factor = (max_font_size - min_font_size) / max_length
    return max(min_font_size, max_font_size - scaling_factor * (length - max_length))

# Function to generate QR Code from participant data
def generate_qr_code_base64(participant):
    qr_data = f"{participant['eId']}-{participant['id']}-{participant['participant_id']}-{participant['first_name']}-{participant['last_name']}-{participant['role']}-{participant['status']}-{participant['contributionStatus']}-{json.dumps(participant['subEvents'])}"
    
    qr = qrcode.make(qr_data)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    
    qr_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{qr_base64}"

@app.route('/print-badge', methods=['POST'])

def print_badge():
    data = request.json
    app.logger.info(f"Received data: {data}")

    # Validate and extract participant details
    participant = data.get('participant', {})
    if not participant or not isinstance(participant, dict):
        app.logger.error('Participant details are required and must be a dictionary')
        return jsonify({'status': 'error', 'message': 'Participant details are required'}), 400

    # Generate the QR Code from participant data
    formattedQrCodeBase64 = generate_qr_code_base64(participant)

    logoBase64 = data.get('logoBase64', '')
    printer = data.get('printer')

    # Validate printer details
    if not printer or not isinstance(printer, dict):
        app.logger.error('Printer details are required and must be a dictionary')
        return jsonify({'status': 'error', 'message': 'Printer details are required'}), 400

    printer_ip = printer.get('ip')
    printer_name = PRINTER_MAP.get(printer_ip)
    if not printer_name:
        app.logger.error('Printer not found for the provided IP address')
        return jsonify({'status': 'error', 'message': 'Printer not found for the provided IP address'}), 400

    # Ensure logoBase64 is properly formatted
    if not logoBase64.startswith("data:image/png;base64,"):
        logoBase64 = f"data:image/png;base64,{logoBase64}"

    # Load and validate the HTML template
    template_path = os.path.join(os.path.dirname(__file__), 'badge_template.html')
    if not os.path.exists(template_path):
        app.logger.error('Badge template file not found')
        return jsonify({'status': 'error', 'message': 'Badge template file not found'}), 500

    with open(template_path, 'r') as file:
        html_template = file.read()

    # Calculate font size for the name
    first_name = participant.get('first_name', 'First Name')
    last_name = participant.get('last_name', 'Last Name')
    full_name = f"{first_name} {last_name}"
    font_size = calculate_font_size(full_name)

    # Render the HTML content
    html_content = render_template_string(
        html_template,
        first_name=first_name,
        last_name=last_name,
        formattedQrCodeBase64=formattedQrCodeBase64,
        logo_html=f'<img src="{logoBase64}" alt="Logo"/>',
        font_size=font_size
    )

    # Save HTML to a file for debugging
    debug_html_path = os.path.join(os.path.dirname(__file__), 'debug_badge.html')
    with open(debug_html_path, "w") as f:
        f.write(html_content)
    app.logger.info("HTML content saved to debug_badge.html for debugging.")

    # Convert HTML to BMP
    bmp_path = os.path.join(os.path.dirname(__file__), 'badge.bmp')
    options = {
        'format': 'bmp',
        'width': 192,
        'height': 312,
        'disable-smart-width': '',
        'zoom': 1.0,
        'enable-local-file-access': ''
    }
    config = imgkit.config(wkhtmltoimage='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')

    try:
        imgkit.from_string(html_content, bmp_path, options=options, config=config)
        if not os.path.exists(bmp_path):
            raise FileNotFoundError('BMP file not created')
        app.logger.info(f"BMP file successfully created at: {bmp_path}")
    except Exception as e:
        app.logger.error(f"Error generating BMP: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to generate BMP'}), 500

    # Simulate print functionality
    # try:
    #     app.logger.info(f"Simulating connection to printer: {printer_name} at {printer_ip}")
    #     # Simulate the print job here
    #     app.logger.info("Simulated print job sent successfully")
    #     return jsonify({'status': 'success', 'message': 'Print job simulated successfully'}), 200
    # except Exception as e:
    #     app.logger.error(f"Error during simulated print: {e}")
    #     return jsonify({'status': 'error', 'message': str(e)}), 500
    
    #Actual Printing Functionality
    try:
      co = evolis.Connection(printer_name, False)

      if not co.is_open():
          print("> Error: can't open printer context.")
          return EXIT_FAILURE
      
      # Set card insertion mode :
      co.set_input_tray(evolis.InputTray.FEEDER)
      # Set card ejection mode :
      co.set_output_tray(evolis.OutputTray.STANDARD)
      # Set card rejection mode :
      co.set_error_tray(evolis.OutputTray.ERROR)
      # Set front and back faces :
      ps = evolis.PrintSession(co)

      if not ps.set_image(evolis.CardFace.FRONT, "badge.bmp"):
          print("> Error: can't load file badge.bmp")
          return EXIT_FAILURE
      
      # Print :
      print("> Start printing...")
      rc = ps.print()
      print(f"> Print result: {rc}.")
      return jsonify({'status': 'success', 'message': 'Print job successful'}), 200
    
    except Exception as e:
      app.logger.error(f"Error during simulated print: {e}")
      return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.logger.info(f"Starting Flask server on IP: {API_IP_ADDRESS} and Port: 5001")
    app.run(host=API_IP_ADDRESS, port=5001, debug=True)
