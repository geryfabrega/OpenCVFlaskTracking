from email.mime import application
import re
from flask import Flask, request, jsonify, after_this_request
import cv2
import numpy as np
import base64
import os

application = Flask(__name__)

@application.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        request.get_data()
        print("Data Recieved")
        try:
            newImage = saveImage(request.data)
            jsonResp = newImage
            response = jsonify(jsonResp)
            response.headers.add('Access-Control-Allow-Origin', '*')
            print("good to go")
            os.remove("output.jpg")
            os.remove("some_image.jpg")
            return response
        except:
            print("No faces found")
            jsonResp = "error"
            response = jsonify(jsonResp)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
            
    if request.method == 'GET':
        print("GOAT IN THE WATER!")
        jsonResp = {'FLSGHJRLGJRSHGKRSJG': 'fglkrjghkrghrkgj'}
        return jsonify(jsonResp)

@application.route('/')
def index():
    return 'Web App with Python Flask!'


def saveImage(data):
    data = data.decode("utf-8")
    data = data.replace("data:image/png;base64,","")
    imgdata = base64.b64decode(data)
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    cascade_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    print("PROGRAM START")
    print("Open Image in local images directory")
    b64image = showImg(face_cascade)
    return b64image

def showImg(face_cascade):
    path = "some_image.jpg"
    img = cv2.imread(path, 0)
    imgColor = cv2.imread(path)
    faces = face_cascade.detectMultiScale(img)
    color = (255,0,255)
    color2 = (0,255,255)
    thickness = 2
    for (x, y, w, h) in faces:
        print("new Image!")
        cv2.rectangle(imgColor, (x, y), (x+w, y+h), color2, thickness)
        cv2.imwrite("output.jpg",imgColor)
    filename2 = 'output.jpg'
    with open(filename2,"rb") as f:
        encodedImg = base64.b64encode(f.read()).decode('ascii')
        sendBack = f'data:image/png;base64,{encodedImg}'
        return sendBack





if __name__ == '__main__':
    application.run(debug=True)