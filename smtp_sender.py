# not working because google closed accessing with email and pass
import smtplib
from email.mime.text import MIMEText

def send_email(message):
    sender = "fif83878@gmail.com"
    password = 'peoplevolkondatrnews'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Test message'
        
        server.sendmail(sender, sender, msg.as_string())

    except Exception as _ex:
        return f"{_ex}\nCheck your login or password"

send_email(message = 'Hello from python')