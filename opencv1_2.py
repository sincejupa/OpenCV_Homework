import cv2 as cv

# 웹캠 열기 (0은 기본 웹캠)
cap = cv.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 그레이스케일 변환
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Canny 에지 검출 (임계값 100, 200)
    edges = cv.Canny(gray, 100, 200)

    # 원본 영상과 에지 검출 영상을 가로로 연결
    combined = cv.hconcat([frame, cv.cvtColor(edges, cv.COLOR_GRAY2BGR)])

    # 결과 출력
    cv.imshow("Original & Canny Edge Detection", combined)

    # 'q' 키를 누르면 종료
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제 및 창 닫기
cap.release()
cv.destroyAllWindows()
