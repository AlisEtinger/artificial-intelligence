#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(r'X:/Users/...')
face_id = input('\n User data input,Look at the camera and wait ...')
count = 0
 
while True: 
 success,img = cap.read() 
 if success is True: 
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
 else: 
 break
 faces = face_detector.detectMultiScale(gray, 1.3, 5)
 for (x, y, w, h) in faces:
 cv2.rectangle(img, (x, y), (x+w, y+w), (255, 0, 0))
 count += 1
 cv2.imwrite("data/User."+str(face_id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w]) 
 cv2.imshow('image',img) 
 k = cv2.waitKey(1) 
 if k == '27':
 break 
 elif count >= 800:
 break
cap.realease()
cv2.destroyAllWindows()
 
import os
import cv2
import numpy as np
from PIL import Image
path = 'data'
recog = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def get_images_and_labels(path):
 image_paths = [os.path.join(path,f) for f in os.listdir(path)]
 face_samples = []
 ids = []
 for image_path in image_paths:
 img = Image.open(image_path).convert('L')
 img_np = np.array(img,'uint8')
 
 if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
  continun 
 id = int(os.path.split(image_path)[-1].split(".")[1])
 faces = detector.detectMultiScale(img_np)
 for(x,y,w,h) in faces:
  face_samples.append(img_np[y:y+h,x:x+w])
  ids.append(id)
 return face_samples,ids
print('Training...')
faces,ids = get_images_and_labels(path)
recog.train(faces,np.array(ids))
recog.save('trainner/trainner.yml')
import cv2
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascade_path = "haarcascade_frontalface_default.xml" 
face_cascade = cv2.CascadeClassifier(cascade_path)
font = cv2.FONT_HERSHEY_SIMPLEX
 
idnum = 0
names = ['1','admin','user1','user2','user3']
 
cam = cv2.VideoCapture(0)
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
 
while True:
 ret,img = cam.read()
 gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(
  gray,
  scaleFactor = 1.2,
  minNeighbors = 5,
  minSize = (int(minW),int(minH))
  )
 for(x,y,w,h) in faces:
 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
 idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w])
 if confidence < 100:
  idum = names[idnum]
  confidence = "{0}%",format(round(100-confidence))
 else:
  idum = "unknown"
  confidence = "{0}%",format(round(100-confidence))
 cv2.putText(img,str(idum),(x+5,y-5),font,1,(0,0,255),1)
 cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(0,0,0),1)
 cv2.imshow('camera',img)
 k = cv2.waitKey(20)
 if k == 27:
  break
cam.release()
cv2.destroyAllWindows()


# In[ ]:




