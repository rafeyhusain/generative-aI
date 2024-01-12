from flask import Flask, render_template, request, redirect, url_for, flash
import openai
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Email configuration
email_config = {
    'sender_email': 'your_email@gmail.com',
    'sender_password': 'your_email_password',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
}

# Prompt for 100-word meeting summary
prompt_summary = "Based on the meeting transcription, please provide a 100-word summary of the meeting."

# Prompt for action item table
prompt_action_items = "Based on the meeting transcription, please provide the action item table, with the action owner and deadlines."

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
    )
    return response.choices[0].text.strip()

def send_email(to_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = email_config['sender_email']
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
        server.starttls()
        server.login(email_config['sender_email'], email_config['sender_password'])
        server.sendmail(email_config['sender_email'], to_email, msg.as_string())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        email = request.form['email']
        text_file = request.files['text_file']

        try:
            # Read the text file
            meeting_transcription = text_file.read().decode('utf-8')

            # Generate meeting summary
            summary = generate_response(prompt_summary)

            # Generate action item table
            action_items = generate_response(prompt_action_items)

            # Send email with meeting summary and action items
            subject = "Meeting Summary and Action Items"
            message = f"Meeting Summary:\n{summary}\n\nAction Items:\n{action_items}"

            send_email(email, subject, message)

            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
