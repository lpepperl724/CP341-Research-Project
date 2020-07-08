import cv2
import os

images = []
ages = []
genders = []

def load_and_resize_images_from_folder(folder):
    for filename in os.listdir(folder):
        try:
            img = cv2.imread(os.path.join(folder,filename))
            img = cv2.resize(img, (100, 100))
            images.append(img)
            extract_gender_and_age(filename)

        except:
            print("i")

def extract_gender_and_age(filename):


    file_name_separator = filename.split('_')

    ages.append(file_name_separator[0])

    genders.append(file_name_separator[1])

load_and_resize_images_from_folder("/Users/mac/Desktop/Clone/CP341-Research-Project/part1")
print(len(ages) == len(genders) == len(images))
