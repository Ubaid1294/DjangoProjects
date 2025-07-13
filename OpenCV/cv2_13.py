import cv2

video = cv2.VideoCapture("images/Nature.mp4")

while video.isOpened():

    _, frame = video.read()

    frame = cv2.resize(frame,(520,520))

    cv2.imshow('Output',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.waitKey(0)
cv2.destroyAllWindows()