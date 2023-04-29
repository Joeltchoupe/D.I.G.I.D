
#WITHOUT DEEP LEARNING

import cv2
 

# loading the test image
image = cv2.imread("kids.jpg")
 
# converting to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# initialize the face recognizer (default face haar cascade)
face_cascade = cv2.CascadeClassifier("cascades/haarcascade_fontalface_default.xml")


# detect all the faces in the image
faces = face_cascade.detectMultiScale(image_gray)
# print the number of faces detected
print(f"{len(faces)} faces detected in the image.")
 

# for every face, draw a blue rectangle
for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

# save the image with rectangles
cv2.imwrite("kids_detected.jpg", image)

#webcam;

import cv2

# create a new cam object
cap = cv2.VideoCapture(0)
# initialize the face recognizer (default face haar cascade)
face_cascade = cv2.CascadeClassifier("cascades/haarcascade_fontalface_default.xml")

while True:
    # read the image from the cam
    _, image = cap.read()
    # converting to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect all the faces in the image
    faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)
    # for every face, draw a blue rectangle
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    cv2.imshow("image", image)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
-------------------------------------------------------------------------------------------------------------------------------------------
#WITH DEEP LEARNING

import cv2
import numpy as np

# https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
prototxt_path = "weights/deploy.prototxt.txt"
# https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20180205_fp16/res10_300x300_ssd_iter_140000_fp16.caffemodel 
model_path = "weights/res10_300x300_ssd_iter_140000_fp16.caffemodel"
 


# load Caffe model
model = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# read the desired image
image = cv2.imread("kids.jpg")
# get width and height of the image
h, w = image.shape[:2]

# preprocess the image: resize and performs mean subtraction
blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
 
# set the image into the input of the neural network
model.setInput(blob)
# perform inference and get the result
output = np.squeeze(model.forward())

font_scale = 1.0
for i in range(0, output.shape[0]):
    # get the confidence
    confidence = output[i, 2]
    # if confidence is above 50%, then draw the surrounding box
    if confidence > 0.5:
        # get the surrounding box cordinates and upscale them to original image
        box = output[i, 3:7] * np.array([w, h, w, h])
        # convert to integers
        start_x, start_y, end_x, end_y = box.astype(np.int)
        # draw the rectangle surrounding the face
        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), color=(255, 0, 0), thickness=2)
        # draw text as well
        cv2.putText(image, f"{confidence*100:.2f}%", (start_x, start_y-5), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), 2)
 

# show the image
cv2.imshow("image", image)
cv2.waitKey(0)
# save the image with rectangles
cv2.imwrite("kids_detected_dnn.jpg", image)
