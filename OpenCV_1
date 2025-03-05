import cv2 as cv
import sys
import numpy as np

img = cv.imread("C:/Users/win/Desktop/soccer.jpg")

if img is None:
    sys.exit("이미지를 불러올 수 없습니다.")

gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray_image_colored = cv.cvtColor(gray_image, cv.COLOR_GRAY2BGR)

combined = np.hstack((img, gray_image_colored))

cv.imshow("Original & Grayscale", combined)
cv.waitKey()
cv.destroyAllWindows()
