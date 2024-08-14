import psutil
import smtplib
from email.mime.text import MIMEText

# Monitor CPU usage and send an alert if it exceeds 90%
cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > 90:
    msg = MIMEText(f"Warning: High CPU usage detected - {cpu_usage}%")
    msg['Subject'] = 'High CPU Usage Alert'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'your_email@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("your_email@example.com", "your_password")
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
