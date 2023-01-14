#pip3 install opencv-python
#opencv github -> https://github.com/opencv/opencv/tree/master/data


# Importing the necessary module which is Opencv
import cv2 as cv
# Creating a cascade classifier object by passing the required path containg the haar cascades .xml files
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Checks whether the path and cascade classifier was loaded correctly
test = face_cascade.load('haarcascade_frontalface_default.xml')

print(test)

if not face_cascade.empty():	# if the casecade object is not empty then continue with the processing
	#print(face_cascade.empty())
	img = cv.VideoCapture(0)	# Captures the video from the webcam/to load a video pass the video path
	while True:
		ret,frame = img.read()	# retrieves frames one by one from the webcam
		# ret is a flag which indicates whether the frame was retreived correctly
		frame = cv.flip(frame, 1)
		gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)		# converts the rgb/bgr frame to gray for processing purposes 
		
		blured = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)	# blurs the gray image to improve detection
		
		faces = face_cascade.detectMultiScale(blured,1.2,9)		# returns the detected faces as rectangle co-ordinates

		for (x,y,w,h) in faces:
			cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)		# Draws retangle on the detected faces
		
		cv.imshow('Face Detection',frame)			

		k = cv.waitKey(3) & 0xff
		if k==27:
			break
	img.release()
	cv.destroyAllWindows()
