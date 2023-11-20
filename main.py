import cv2

image_path = 'cat.jpeg'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = face_cascade



cv2.imshow("Cat", image)
cv2.waitKey()