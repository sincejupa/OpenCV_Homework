import cv2 as cv
import sys
import numpy as np

# 이미지 불러오기
img = cv.imread("C:/Users/win/Desktop/soccer.jpg")

# 이미지가 정상적으로 로드되었는지 확인
if img is None:
    sys.exit("이미지를 불러올 수 없습니다.")
    
# 그레이스케일 변환
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 원본(BGR)과 그레이스케일을 같은 채널 수(3채널)로 맞추기 위해 변환
gray_image_colored = cv.cvtColor(gray_image, cv.COLOR_GRAY2BGR)

# 두 이미지를 가로로 연결
combined = np.hstack((img, gray_image_colored))

# 결과 출력
cv.imshow("Original & Grayscale", combined)
cv.waitKey()
cv.destroyAllWindows()
