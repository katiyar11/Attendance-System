from imutils.video import VideoStream
import imutils
import cv2
import os
import numpy as np
from django.contrib import messages
from django.conf import settings
from datetime import datetime

path= os.path.join(settings.BASE_DIR,'static/images')
saved_img= os.path.join(settings.BASE_DIR,'Registered_users/Admin')


def get_frame_now(username):
    cap = cv2.VideoCapture(0)
    a=0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st=str(a)
        if a<50:
            gray = cv2.putText(gray, 'Photos has saved={0}'.format(st), (10, 100), font, 1, (0, 0, 0), 4, cv2.LINE_AA) 
            cv2.imwrite(os.path.join(saved_img, username+'_%d.jpg') % a, gray)
        else:
            msg="User Added"
            frame = cv2.putText(gray, msg.format(st), (10, 100), font, 1, (0, 0, 0), 4, cv2.LINE_AA)
            
        a+=1
        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    





 # 