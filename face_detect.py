import cvlib as cv
import cv2
import numpy as np
import os

img_height = 96
img_width = 96

def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        try:
            img = cv2.imread(os.path.join(folder,filename))
            extract_face(img, filename)
        except:
            pass

def extract_face(image, filename):

    face, confidence = cv.detect_face(image)

    for idx, f in enumerate(face):
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]
        face_crop = np.copy(image[startY:endY,startX:endX])
        face_crop = cv2.resize(face_crop, (img_height, img_width))
        #face_crop = face_crop.astype("float") / 255.0
        #face_crop = img_to_array(face_crop)
        cv2.imwrite('/Users/mac/Desktop/Clone/CP341-Research-Project/Faces/' + filename, face_crop)

load_images_from_folder('/Users/mac/Desktop/Clone/CP341-Research-Project/part1')
