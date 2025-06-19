import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


smtp_port = 587                 
smtp_server = "smtp.gmail.com"  

email_from = "transcendence@sjbhs.edu.in"

email_list = [
    "sambantia07@gmail.com",
    "agarwalom24@gmail.com"
]

pswd = "vgdsrsjbpgccnkau" 


subject = "Transcendence 2024 invite"



def send_emails(email_list):

    for person in email_list:

        body = f"""
        Dear Sir/Madam,

        St Joseph’s Boys’ High School is elated to officially invite you to the 8th edition of its
        annual science fest, Transcendence 2024.

        We would be honored to have you join us for this exciting and celebrated fest. Your
        presence would add immense value to the event and contribute to its success.
        Attached are the invitation and event brochure furnished with necessary details. Please
        feel free to reach out to us with further queries.
        We look forward to hosting you at Transcendence 2024.

        Warm regards,
        Team Transcendence.
        """

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        
        filename = "Transcendence 2024 Brochure.pdf"


        attachment= open(filename, 'rb') 


        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        text = msg.as_string()

        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    TIE_server.quit()

send_emails(email_list)