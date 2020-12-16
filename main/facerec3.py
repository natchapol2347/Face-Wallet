import face_recognition
import cv2
# import pymongo
import os
import time
import requests
import sys
import json
import requests


#url = '127.0.0.1' #for this computer
#url = '192.168.1.55' #for other computer
url = '172.20.10.13' #for raspberrypi


def facerec():
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    # instead of put the hard codes put something dynamic to connect it with the tkinter
    images=os.listdir("face")
    #print(x)
    if '.DS_Store' in images:
        images.remove('.DS_Store')
    #print (images)
    known_face_encodings = []
    known_face_names = []
    for i in images:

        image = face_recognition.load_image_file('face/'+i)
        face_encoding = face_recognition.face_encodings(image)[0]

        known_face_encodings.append(face_encoding)
        known_face_names.append(os.path.splitext(i)[0])
    print(known_face_names)


    # input picture take this session
    # Create arrays of known face encodings and their names
      #put username in tkinter in this 

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    count_open=0
    count_close=0
    #time count
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            face_names = []
            
            for face_encoding in face_encodings:
                # See if the face is a match for the known face
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
                #tolerance will increase the strict of face regcognition

                name = "Unknown"
                 
                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    time.sleep(0.05)
                #    conv = '1'
                #    res = requests.post("http://" + url + ":5000/", data=conv)
                #    print(res.text)
                    count_open += 1
                if count_open==5:
                    try:
                        x = requests.get('http://'+url+':5000/', timeout=1)
                        print(x)
                        break
                    except requests.exceptions.ReadTimeout:
                        pass
                    count_open=0
                # use time.sleep to count the time and count until 9 then the door will open
                if name == "Unknown":
                    time.sleep(0.05)
                    count_close += 1
                if count_close ==5:
                    (requests.get('http://'+url+':5000/').text)
                    #conv = '0'
                    #res = requests.post("http://" + url + ":5000/", data=conv)
                    #print(res.text)
                    print ("Error! 404!")
                    count_close=0
                
                # use time.sleep to count the time and count until 9 then the door will open
                face_names.append(name)
    
                        

        process_this_frame = not process_this_frame
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            global font
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # text show to exit
        cv2.putText(frame,'Press "E" to exit ',(200,50), cv2.FONT_HERSHEY_DUPLEX, 2,(255,255,255),2,cv2.LINE_AA)

        # Display the resulting image
        cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

#facerec()