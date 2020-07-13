from keras.preprocessing.image import img_to_array
import cvlib as cv
import cv2
import numpy as np
import os

img_height = 96
img_width = 96
channels = 3

images = []
ages = []
genders = []

def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        try:
            img = cv2.imread(os.path.join(folder,filename))
            img = img.astype("float") / 255.0
            img = img_to_array(img)
            if img.shape == (img_height, img_width, channels):
                images.append(img)
                extract_age_and_gender(filename)
        except:
            pass

#Extract age and gender from the iamge's filename
def extract_age_and_gender(filename):

    file_name_separator = filename.split('_')

    #Save ages and genders into corresponding lists
    ages.append(int(file_name_separator[0]))

    genders.append(int(file_name_separator[1]))

load_images_from_folder('/Users/mac/Desktop/Clone/CP341-Research-Project/Faces')

images = np.array(images)

ages = np.array(ages)

genders = np.array(genders)
