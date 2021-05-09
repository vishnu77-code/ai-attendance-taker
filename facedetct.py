import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime
global n1
path="New folder"
images=[]
classname=[]
list=os.listdir(path)
for cl in list:
    cur_img=cv2.imread(f"{path}/{cl}")
    images.append(cur_img)
    classname.append(os.path.splitext(cl)[0])
def findencode(images):
    encode_list=[]
    for imgS in images:
        imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
        faceencode=face_recognition.face_encodings(imgS)[0]
        encode_list.append(faceencode)
    return encode_list

def markattendance(names):
   with open("attendance.csv","r+") as f:
        myDataList=f.readlines()
        name_list=[]



        for line in myDataList:
            nameo=line.split(",")
            print(nameo)
            name_list.append(nameo[0])
        if names not in name_list:
                now=datetime.now()
                time=now.strftime(f"%H:%M:%S")
                f.writelines(f"{names},{time}")


encodelistknown=findencode(images)








cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    im=cv2.resize(img,(0,0),None,0.25,0.25)
    im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    faceloc=face_recognition.face_locations(im)
    faceenco=face_recognition.face_encodings(im,faceloc)
    for f ,fa in zip(faceenco,faceloc):
        matches=face_recognition.compare_faces(encodelistknown,f)
        matcloc=face_recognition.face_distance(encodelistknown,f)
        matchindex=np.argmin(matcloc)
        if matches[matchindex]:
            name=classname[matchindex].upper()
            print(name)
            x1,y1,x2,y2=fa
            x1, y1 , x2 , y2 =x1*4,y1* 4,x2* 4,y2* 4
            cv2.rectangle(img,(y2,x1),(y1,x2),(0,255,0),2)
            cv2.rectangle(img, (y2 , x2-35 ), (y1 , x2 ), (0, 255, 0), cv2.FILLED)
            cv2.putText(img,name,(y2+6,x2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattendance(name)
    cv2.imshow("webcam",img)
    cv2.waitKey(1)

