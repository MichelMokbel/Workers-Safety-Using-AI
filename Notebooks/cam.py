import cv2

# Open the first camera connected to the computer
cap = cv2.VideoCapture(0)  # or the index of your camera
if not cap.isOpened():
    print("Cannot open camera")
    exit()
# Try to get the first frame
ret, frame = cap.read()
if ret:
    cv2.imshow('Camera Test', frame)
    cv2.waitKey(0)  # Wait for a key press to close the window
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
