import cv2
import numpy as np

if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt2.xml')

    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for(x,y,w,h) in faces:
            print(x,y,w,h)
            roi_gray = gray[y:y+h, x:x+w] #y_start -> y_end, x_start -> x_end von unten
            roi_color = frame[y:y+h, x:x+w]
            img_item = "my-image.png"
            cv2.imwrite(img_item, roi_gray)

            color = (255, 0, 255) #BGR Achtung! kein RGB
            stroke = 3 #Dicke der Linie
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        cv2.imshow('frame', frame)

        if(cv2.waitKey(20) & 0xFF == ord('q')):
            break

cap.release()
cv2.destroyAllWindows()