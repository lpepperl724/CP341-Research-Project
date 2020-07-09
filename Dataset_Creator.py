import numpy as np
import os
from PIL import Image, ImageOps

images = []
ages = []
genders = []

def load_and_resize_images_from_folder(folder):
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        img = ImageOps.grayscale(img)
        img = img.resize((100, 100))
        imgarr = np.array(img)
        images.append(imgarr)
        extract_gender_and_age(filename)
        img.close()

def extract_gender_and_age(filename):

    file_name_separator = filename.split('_')

    ages.append(int(file_name_separator[0]))

    genders.append(int(file_name_separator[1]))

images = np.array(images)

ages = np.array(ages)

genders = np.array(genders)
