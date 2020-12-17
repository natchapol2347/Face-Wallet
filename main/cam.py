import cv2

# Windows dependencies
# - Python 2.7.6: http://www.python.org/download/
# - OpenCV: http://opencv.org/
# - Numpy -- get numpy from here because the official builds don't support x64:
#   http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

# Mac Dependencies
# - brew install python
# - pip install numpy
# - brew tap homebrew/science
# - brew install opencv
def cam(name):
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while(True):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        cv2.putText(rgb, 'Press "Q" to take a picture',(200,50), font, 2,(255,255,255),2,cv2.LINE_AA)
        
        cv2.imshow('frame', rgb)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            out = cv2.imwrite("face/"+ name+'.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()
#cam('may')
