import cv2


#load the cascade
face_cascade = cv2.CascadeClassifier(r"D:\openCV\sources\data\haarcascades\haarcascade_frontalface_default.xml")


#loading the image 
#img = cv2.imread("Sample_image.jpg")

#load the video
cap = cv2.VideoCapture(0)

while True:
#reading frame from video
 success,img = cap.read()

 #converting BGR image to GRAY image
 gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

 #showing gray image
 cv2.imshow("gray image", gray)

 #detects the faces in input image
 faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,
    minNeighbors=6, minSize=(60, 60))

 #drawing rectangles to detected faces 
 for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w , y+h),(255,0,0),2)

 #showing output image 
 cv2.imshow("output image", img)
 #if want to save the output image in system used the below statement
 #cv2.imwrite("output.jpg",img)

#getting out of the infinity loop
 k = cv2.waitKey(1)
 if k == 13:
     break

#to close the camera
cap.release()
cv2.destroyAllWindows()

