import smtplib
from email.mime.text import MIMEText

def email_notification(request):
    try:
        # Get the email details from the request
        email_details = request.form

        # Create a SMTP connection
        smtp_connection = smtplib.SMTP("YOUR_SMTP_SERVER", 587)
        smtp_connection.starttls()
        smtp_connection.login("YOUR_EMAIL_ADDRESS", "YOUR_EMAIL_PASSWORD")

        # Create a text message
        message = MIMEText("Your order has been placed successfully!")
        message["Subject"] = "Order Confirmation"
        message["From"] = "YOUR_EMAIL_ADDRESS"
        message["To"] = email_details["email"]

        # Send the email
        smtp_connection.sendmail("YOUR_EMAIL_ADDRESS", email_details["email"], message.as_string())
        smtp_connection.quit()

        # Return a success message
        return "Email sent successfully!"
    except Exception as e:
        # Handle any errors that occur during email notification
        print(f"Error sending email: {e}")
        return None
