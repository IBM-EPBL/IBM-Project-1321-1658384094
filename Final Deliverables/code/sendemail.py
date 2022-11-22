import smtplib
import sendgrid as sg
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "personal expense tracker"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    from_email = Email("kganeshkumar011@gmail.com") 
    to_email = To(email) 
    subject = "Email Sent with SendGrid"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)
    try:
        sg=SendGridAPIClient('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')
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
   