import numpy as np
import os
from PIL import Image

class Dataset_Creator:
    def __init__(self):
        self.images = []
        self.ages = []
        self.genders = []
        self.combined = []
        
    def load_and_resize_images_from_folder(self, folder, width, height):
        i = 0
        for filename in os.listdir(folder):
            img = Image.open(os.path.join(folder,filename))
            img = img.resize((width, height))
            imgarr = np.array(img)
            #Filter out gray images
            if imgarr.shape == (width, height, 3):
                self.images.append(imgarr)
                self.extract_age_and_gender(filename)
            img.close()
            #temp fix for getting a smaller sample of the data
            if i > 500:
                break
            i+=1

    #Extract age and gender from the images's filename
    def extract_age_and_gender(self, filename):
        file_name_separator = filename.split('_')
        age = int(file_name_separator[0])
        gender = int(file_name_separator[1])
        #Save ages and genders into corresponding lists
        self.genders.append(gender)
        self.ages.append(age)  
        
    def getData(self, path, width, height):
        self.load_and_resize_images_from_folder(path, width, height)
        self.images = np.array(self.images)
        self.ages = np.array(self.ages)
        self.genders = np.array(self.genders)
        return self.images, self.genders, self.ages
        
