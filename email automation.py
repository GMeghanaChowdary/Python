import smtplib
from email.mime.text import MIMEText
def send_email():
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    subject = "Test Email"
    body = "This is a test email."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, "your_password")
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
send_email()
