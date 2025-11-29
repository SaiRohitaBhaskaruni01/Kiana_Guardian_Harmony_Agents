import requests

import smtplib
from email.mime.text import MIMEText

def send_email_alert(to_emails, subject, body):
    from_email = st.secrets["email"]["from_email"]
    password = st.secrets["email"]["password"]

    for to_email in to_emails:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        st.success(f"Email sent to {to_email}")




import pandas as pd

df = pd.read_csv("health_metrics.csv")
# manager_email = "ps12049@usc.edu"
manager_email = "xieqingz@usc.edu"
# manager_email = "bhaskaru@usc.edu"

abnormal_entries = []

for _, row in df.iterrows():
    hr = row['heart_rate_bpm']
    temp = row['body_temperature_c']
    
    if hr < 50 or hr > 105 or temp < 33 or temp > 40:
        abnormal_entries.append(
            f"Employee {row['employee_id']} ({row['employee_name']}): "
            f"HR={hr} BPM, Temp={temp}°C"
        )

# Send a single consolidated email
if abnormal_entries:
    full_message = "Abnormal Health Metrics Detected:\n\n" + "\n".join(abnormal_entries)
    send_email_alert(manager_email, "Abnormal Health Alert", full_message)