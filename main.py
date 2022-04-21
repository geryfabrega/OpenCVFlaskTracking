import cv2
import pytesseract
import numpy as np
from torchvision.models import detection
import torch

def main():
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    cascade_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    print("PROGRAM START")
    print("Open Image in local images directory")
    showImg(face_cascade)

def showImg(face_cascade):
    path = "../images/image8.png"
    img = cv2.imread(path, 0)
    cv2.imshow('image', img)
    faces = face_cascade.detectMultiScale(img)
    color = (255,0,255)
    color2 = (0,255,255)
    thickness = 1
    box_ratio = .22
    print(text)
    for (x, y, w, h) in faces:
        h2 = int(h * box_ratio)
        # cv2.rectangle(img, (x, y-h2), (x+w, y+h2), color2, thickness)
        crop_img = img[y - h2:y+h2, x:x+w]
        crop_img = cv2.threshold(crop_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        cv2.imshow('image', crop_img)
        text = pytesseract.image_to_string(crop_img)
        print(text)
        cv2.waitKey(0)
    print(text)

if __name__ == "__main__":
    main()