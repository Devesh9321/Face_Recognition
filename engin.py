
import face_recognition
import cv2
import csv
import os
import numpy as np

from datetime import datetime

class Engin:

    detector = cv2.CascadeClassifier('config/haarcascade_frontalface_default.xml')
    now = datetime.now()
    current_time = now.strftime('%H-%M-%S')
    current_date = now.strftime('%d-%m-%y')
    Exection = True
    name = ''
    data_pred_dict = { 'name': [], 'encoding': []  }
    atten_data = { 'Name':[], 'Time':[]  }

    for path in os.listdir('./Data'):
        data_pred_dict['name'].append(path.replace('.png',''))
        tar_img = face_recognition.load_image_file('Data/'+path)
        data_pred_dict['encoding'].append(face_recognition.face_encodings(tar_img)[0])

    students = data_pred_dict['name'].copy()
    
    def __init___(self):
        # print(self.data_pred_dict)
        pass

    def temp (self):
        print(self.data_pred_dict)
        pass

    def mark_atten(self,data:dict):
        with open('Attendance/Attendance_'+self.current_date+'.csv', 'a+') as csvfile:
        # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames = ['Name','Time'])
            writer.writeheader()
            writer.writerow(data)
    
    def start_cam(self):
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(3, 640) 
        cam.set(4, 480) 
        return cam

    def destroy(self,cam):
        cam.release()
        cv2.destroyAllWindows()
    
    def varify_atten(self):
        cam = self.start_cam()

        try:
            while self.Exection:
                if len(self.students) == 0:
                    break

                ret, img = cam.read() 

                small_frame = cv2.resize(img,(0,0),fx=0.25,fy=0.25)
                face_location = face_recognition.face_locations(small_frame)
                face_encode = face_recognition.face_encodings(small_frame,face_location)

                for face_encoded  in face_encode:
                    matcher = face_recognition.compare_faces(self.data_pred_dict['encoding'],face_encoded)
                    face_distance = face_recognition.face_distance(self.data_pred_dict['encoding'],face_encoded)
                    best_match_index = np.argmax(matcher)
                    
                    if matcher[best_match_index]:
                        self.name = self.data_pred_dict['name'][best_match_index]

                    if self.name in self.data_pred_dict['name']:
                        if self.name in self.students:
                            self.atten_data['Name'].append(self.name)
                            self.atten_data['Time'].append(self.current_time)
                            self.students.remove(self.name)
                # cv2.imshow('camera',img) 
                self.Exection = False
                        
            self.mark_atten(self.atten_data)

            self.destroy(cam)

        except Exception as e:
            self.destroy(cam)
            print('Error : ',e)
            exit()

    def Add_std(self):

        face_id = input("Enter a Numeric user ID Code here:  ")
        if len(face_id)==7 :
            
            input(f'Please stand along Std_id : {face_id} before the camara (Press `Enter` to Start ).............')
            cam = self.start_cam()

            ret, img = cam.read() 
            converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            faces = self.detector.detectMultiScale(converted_image, 1.3, 5)

            for (x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                
                cv2.imwrite("Data/" + str(face_id) + ".png", converted_image[y:y+h,x:x+w])

            cv2.imshow('image', img)
            
            self.destroy(cam)

        else:
            print('Enter Valid Input File name ! Please try in this format `ex. 20CM041`')