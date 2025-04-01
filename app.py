from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

EMAIL_USER = 'hospital.carecloud@gmail.com'
EMAIL_PASSWORD = 'wkig gfnc ohcq ywso'  # Use an App Password if needed
RECIPIENT_EMAIL = 'adevadiga2005@gmail.com'

@app.route('/report-bug', methods=['POST'])
def report_bug():
    try:
        data = request.json  # Get JSON data from request
        message = data.get('message', '')
        
        if not message.strip():
            return jsonify({"error": "Message cannot be empty"}), 400
        
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = "Bug Report from Mobile App"
        
        body = f"Bug Report:\n\n{message}"
        msg.attach(MIMEText(body, 'plain'))
        
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, RECIPIENT_EMAIL, msg.as_string())
        server.quit()

        return jsonify({"message": "Bug report sent successfully!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
