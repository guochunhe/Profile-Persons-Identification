from imutils import face_utils
import dlib
import cv2
import numpy as np

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

def detect_landmarks(file):
    # load the input image and convert it to grayscale
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    rects = detector(gray, 0)

    # loop over the face detections
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        needed = [shape[33], shape[8], shape[36], shape[45], shape[48], shape[54]]
        # loop over the (x, y)-coordinates for the facial landmarks and draw them on the image
        for (x, y) in needed:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

    # show the output image with the face detections + facial landmarks
    cv2.imwrite('new' + file, image)

detect_landmarks("1.jpg")
#detect_landmarks("2.jpg")