import cv2
import numpy as np

img = cv2.imread("start_opencv_dog.jpg")

if img is None:
    print("Image not loaded")
else:
    print("Image shape:", img.shape)

    imgCropped = img[0:200, 0:300]

    if imgCropped is None or imgCropped.size == 0:
        print("Cropped image is empty")
    else:
        cv2.imshow("Image Cropped", imgCropped)
        cv2.waitKey(0)