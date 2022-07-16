import cv2 # opencv-python install package
#new image in gray scale 
color= cv2.imread("galaxy.jpeg", 2)
cv2.imwrite("galaxy-gray.jpeg", color)
