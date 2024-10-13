from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'    # Replace with your email password or app password
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    search_query = data.get('searchQuery')
    number_of_photos = data.get('numberOfPhotos')
    email = data.get('email')

    if not search_query or not number_of_photos or not email:
        return jsonify({'message': 'All fields are required.'}), 400

    msg = Message('Photo Search Submission', recipients=[email])
    msg.body = f'Search Query: {search_query}\nNumber of Photos: {number_of_photos}'

    try:
        mail.send(msg)
        return jsonify({'message': 'Submission successful!'}), 200
    except Exception as e:
        return jsonify({'message': 'Error sending email.', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)
