import cv2
from fpdf import FPDF
import os
# IP address of web stream from mobile device
url="http://192.168.0.145:8080/video"
cap=cv2.VideoCapture(url)
ret=True
f1=0
i=0
while ret:
    ret, frame=cap.read()
    if f1==0:
        # enter action
        print("press s to scan")
        print('press q to quit')
        f1=f1+1
    cv2.imshow("camera feed",frame)
    k=cv2.waitKey(1)
    if k==ord('s'):
        # ends stream and captures image
        cv2.destroyWindow("camera feed")
        cv2.imshow("scanned photo",frame)
        print("press u if unreadable")
        print("press b for black and white")
        k1=cv2.waitKey(0)
        if k1==ord('u'):
            # using adaptive thresholding on captured image if it is unreadable
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            new=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,255,1)
            cv2.imwrite("E://pdf//scanned%d.jpg"%i,new)
            i=i+1
            continue
        elif k1==ord('b'):
            # saving grayscale image
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imwrite("E://pdf//scanned%d.jpg"%i,gray)
            i=i+1
            print('press s to scan')
            print('press q to quit')
            continue
    if k==ord('q'):
        # ending stream
        ret=False
        break
cv2.destroyAllWindows()
imagelist=os.listdir("E://pdf")
pdf=FPDF()
for image in imagelist:
    # saving pdf
    image="E://PDF//"+image
    pdf.add_page()
    pdf.image(image)
# output
pdf.output("E://your_file.pdf","F")

