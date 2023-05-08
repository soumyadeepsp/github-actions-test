import smtplib, ssl
import os
port = 465
smtp_server = "smtp.gmail.com"
USEREMAIL = "soumyadeepsp@gmail.com"
PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")
message = """\
    Subject: Github Email Report
    This is your daily email report.    
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USEREMAIL, PASSWORD)
    server.sendmail(USEREMAIL, "soumyadeep18104@iiitd.ac.in", message)