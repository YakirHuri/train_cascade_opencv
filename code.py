import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)

bootle_cascade=cv2.CascadeClassifier('/home/yakir/bottle/images/negative/output/cascade.xml')

count =1
while(True):
	#img=cv2.imread('/home/yakir/bottle/images/positive/resize/'+str(count)+'.jpg')
	ret, img = cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	font=cv2.FONT_HERSHEY_SIMPLEX
	faces=bootle_cascade.detectMultiScale(gray,1.345,5,75)


	for(x,y,w,h) in faces:
		img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(img,'b',(x,y),font,0.9,(0,255,0),2)
		print('faces')

	cv2.imshow("b", img) 
	cv2.waitKey(0)  
	# p,l,m=cv2.split(img)
	# img=cv2.merge([m,l,p])

	# plt.imshow(img)
	# plt.show()
	# cv2.waitKey(0)
