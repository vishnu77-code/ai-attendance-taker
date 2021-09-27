import dlib
import face_recognition
import cv2
import numpy
k=face_recognition.load_image_file("googleceo.jpg")
k=cv2.cvtColor(k,cv2.COLOR_BGR2RGB)
k1=face_recognition.load_image_file("Elon_Musk.jpg")
k1=cv2.cvtColor(k1,cv2.COLOR_BGR2RGB)
coordinates=face_recognition.face_locations(k)
encoding=face_recognition.face_encodings(k)[0]
coordinates1=face_recognition.face_locations(k1)
encoding1=face_recognition.face_encodings(k1)[0]
(x,y,w,h)=coordinates[0]

rect=cv2.rectangle(k,(h,x),(y,w),(0,255,0),2)
(x,y,w,h)=coordinates1[0]
rect1=cv2.rectangle(k1,(h,x),(y,w),(0,255,0),2)
result=face_recognition.compare_faces([encoding],encoding1)
cv2.imshow("face datector",k)
cv2.imshow("facedete",k1)
print(result)
cv2.waitKey(0)
from datetime import datetime
import pytz
tz="Asia/kolkata"
t=pytz.timezone(tz)
time=datetime.now(t).time()
tim=datetime.now()
if tim.hour==12:
    print("patti")
else:
    pass
print(time)


