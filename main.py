import cv2

image_path = 'cat.jpeg'
face_cascade = cv2.CascadeClassifier
image = cv2.imread(image_path)




cv2.imshow("Cat", image)
cv2.waitKey()