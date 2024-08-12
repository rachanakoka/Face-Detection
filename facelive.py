import cv2
face_detector1 = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml') 
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#converting to gray
    faces = face_detector1.detectMultiScale(gray,1.1,4)
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, pt1 =(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness= 3)
        roi_gray = gray[y:y+h,x:x+w]
        cv2.imshow("window",frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break 