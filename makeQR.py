import roll
import qrcode
import mail

# pip3 install opencv-python qrcode numpy Image
# pip3 install opencv-python
# pip3 install qrcode
# pip3 install numpy

# For start server open terminal and type below written command
#  python -m smtpd -c DebuggingServer -n localhost:1025

obj = roll.roll_Gen()
mailObj = mail.send_Mail()

Reciever_Email = input("Enter your email: ")
n = int(input("Enter school roll number: "))
ch = input("Enter your correct choice from flowlling:--"
                       "\n1.Andhra Pradesh\n2.Bihar\n3.Maharashtra\n4.Uttar Pradesh\n5.West Bengal\nPlease Enter number only: ")

data, state = obj.gen(n, ch)

if(data!="NULL"):
    QRCodefile = "MUOQRCode.png"
    QRimage = qrcode.make(data)
else:
    print("Wrong Input! ! !")

# Saving image into a file
QRimage.save(QRCodefile)

mailObj.email(Reciever_Email, data, state)

print("\nPlease check your email[{}] for barcode\nThank you".format(Reciever_Email))