import cv2
import numpy as np

# 전역 변수 설정
drawing = False  # 드래그 중 여부
ix, iy = -1, -1  # 시작 좌표
roi = None  # 선택한 영역

# 마우스 이벤트 처리 함수
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, roi, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 클릭 시 시작 좌표 저장
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # 드래그 중이면 사각형 그리기
        if drawing:
            img_copy = img.copy()  # 원본 이미지를 유지하면서 업데이트
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("Image", img_copy)

    elif event == cv2.EVENT_LBUTTONUP:  # 마우스 버튼을 놓으면 ROI 저장
        drawing = False
        roi = img[iy:y, ix:x]  # numpy 슬라이싱으로 ROI 추출
        if roi.size > 0:  # 유효한 영역만 출력
            cv2.imshow("ROI", roi)

# 이미지 불러오기
img = cv2.imread("soccer.jpg")
img_copy = img.copy()

cv2.imshow("Image", img)
cv2.setMouseCallback("Image", draw_rectangle)

# 키 지정
while True:
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):  # r 키를 누르면 초기화
        img_copy = img.copy()
        roi = None
        cv2.imshow("Image", img_copy)

    elif key == ord("s") and roi is not None:  # s 키를 누르면 ROI 저장
        cv2.imwrite("roi.jpg", roi)
        print("ROI 저장 완료: roi.jpg")

    elif key == 27:  # ESC 키를 누르면 종료
        break

cv2.destroyAllWindows()
