import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

# Twilio credentials
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
twilio_number = 'your_twilio_phone_number'

# Email credentials
email_address = 'your_email_address'
email_password = 'your_email_password'

def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp_via_sms(phone_number, otp):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your OTP is: {otp}',
        from_=twilio_number,
        to=phone_number
    )
    print("OTP sent successfully via SMS.")

def send_otp_via_email(email, otp):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email
    msg['Subject'] = 'Your OTP'

    body = f'Your OTP is: {otp}'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)
    text = msg.as_string()
    server.sendmail(email_address, email, text)
    server.quit()
    print("OTP sent successfully via Email.")

def verify_otp(otp, entered_otp):
    return otp == entered_otp

def main():
    # Get mobile number and email address
    phone_number = input("Enter your mobile number: ")
    email = input("Enter your email address: ")

    # Generate OTP
    otp = generate_otp()

    # Send OTP via SMS
    send_otp_via_sms(phone_number, otp)

    # Send OTP via Email
    send_otp_via_email(email, otp)

    # Verify OTP
    entered_otp = input("Enter the OTP sent to your mobile and email: ")
    if verify_otp(otp, entered_otp):
        print("OTP verified successfully.")
    else:
        print("OTP verification failed.")

if _name_ == "_main_":
    main()
