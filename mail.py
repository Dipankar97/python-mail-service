import smtplib, ssl
import imghdr
from email.message import EmailMessage

# For start server open terminal and type below written command
#  python -m smtpd -c DebuggingServer -n localhost:1025

class send_Mail:
    def email(self, Reciever_Email, data, state):
        Sender_Email = "dnoreply17@gmail.com"
        Password = "Dipankar@00"

        newMessage = EmailMessage()
        newMessage['Subject'] = "Your {} Roll Number".format(state)
        newMessage['From'] = Sender_Email
        newMessage['To'] = Reciever_Email
        newMessage.set_content('Your unique roll for {} state is {}\nHere you can find your bar-code for entry.\nDo not share with anyone...'.format(state, data))

        files = ['MUOQRCode.png']

        for file in files:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name
            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)

