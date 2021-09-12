import cv2
from pyzbar.pyzbar import decode
import time
import os
# need to install "opencv,pyzbar"

def main():

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)     #3 - Width
    cap.set(4, 480)     #4 - Height
    # used_Cods = []
    r = ""
    d = ""
    camera = True

    while camera == True:
        success, frame = cap.read()
        if not os.path.exists("store_Roll.txt"):
            f = open("store_Roll.txt","w")
            f.close()
        else:
            f = open("store_Roll.txt","r")
            r = f.read()
            f.close()

        for code in decode(frame):
            if code.data.decode('utf-8') not in r:
                print("Approved. You can enter!")
                print(code.data.decode('utf-8'))
                # used_Cods.append(code.data.decode('utf-8'))
                f = open("store_Roll.txt", "a")
                d = code.data.decode('utf-8')
                f.write("\n{}".format(d))
                f.close()
                time.sleep(5)
            elif code.data.decode('utf-8') in r:
                print("Sorry, this QR already used!")
                time.sleep(5)
        cv2.imshow('Scan-Window', frame)
        cv2.waitKey(1)


if __name__ == "__main__":
   main()

