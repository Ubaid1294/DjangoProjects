import cv2

video = cv2.VideoCapture("images/Nature.mp4")

frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

output = cv2.VideoWriter('images/output.mp4',fourcc,fps,(frame_width,frame_height))

while(video.isOpened()):
    ret,frame = video.read()
    if not ret:
        break
    output.write(frame)
    cv2.imshow('Output',frame)

    if cv2.waitKey(25) & 0xFF == ord('s'):
        break

output.release()
cv2.destroyAllWindows()

# import cv2
#
# video = cv2.VideoCapture("images/Nature.mp4")
#
# if not video.isOpened():
#     print("Could not open video file.")
#     exit()
#
# # Get actual video dimensions
# frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = video.get(cv2.CAP_PROP_FPS)
#
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output = cv2.VideoWriter('images/output.mp4', fourcc, fps, (frame_width, frame_height))
#
# while True:
#     ret, frame = video.read()
#     if not ret:
#         print("📌 No more frames or failed to read the video.")
#         break
#
#     output.write(frame)
#     cv2.imshow('Output', frame)
#
#     if cv2.waitKey(25) & 0xFF == ord('s'):  # Press 's' to stop
#         break
#
# video.release()
# output.release()
# cv2.destroyAllWindows()