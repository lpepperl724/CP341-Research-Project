import numpy as np
import os
from PIL import Image

images = []
ages = []
genders = []

def load_and_resize_images_from_folder(folder):
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        img = img.resize((100, 100))
        imgarr = np.array(img)
        #Filter out gray images
        if imgarr.shape == (100, 100, 3):
            images.append(imgarr)
            extract_age_and_gender(filename)
        img.close()

#Extract age and gender from the iamge's filename
def extract_age_and_gender(filename):

    file_name_separator = filename.split('_')

    #Save ages and genders into corresponding lists
    ages.append(int(file_name_separator[0]))

    genders.append(int(file_name_separator[1]))

images = np.array(images)

ages = np.array(ages)

genders = np.array(genders)
