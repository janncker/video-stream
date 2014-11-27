import time
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade.xml")

class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
	self.cam = cv2.VideoCapture(0) 	
	self.cam.set(3, 320)
	self.cam.set(4, 240)
	time.sleep(1)

    def get_frame(self):
	ret, img = self.cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

	ret2, jpeg = cv2.imencode('.jpg', img)
	return jpeg.tostring() 

    def __del__(self):
	self.cam.release()
