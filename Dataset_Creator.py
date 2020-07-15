import numpy as np
import os
import random
from PIL import Image

class Dataset_Creator:
    def __init__(self):
        self.images = []
        self.ages = []
        self.genders = []
        self.combined = []
        
    def load_and_resize_images_from_folder(self, folder, width, height, max_data):
        files = os.listdir(folder)
        num_files = len(files)
        if max_data > num_files:
            max_data = num_files
        dataindex = random.sample(range(num_files), max_data)
        
        for fileindex in dataindex:
            filename = files[fileindex]
            img = Image.open(os.path.join(folder,filename))
            img = img.resize((width, height))
            imgarr = np.array(img)
            #Filter out gray images
            if imgarr.shape == (width, height, 3):
                self.images.append(imgarr)
                self.extract_age_and_gender(filename)
            img.close()

    #Extract age and gender from the images's filename
    def extract_age_and_gender(self, filename):
        file_name_separator = filename.split('_')
        age = int(file_name_separator[0])
        gender = int(file_name_separator[1])
        #Save ages and genders into corresponding lists
        self.genders.append(gender)
        self.ages.append(age)  
    
    #call other methods and return the data
    def getData(self, folder, width, height, max_data):
        self.load_and_resize_images_from_folder(folder, width, height, max_data)
        self.images = np.array(self.images)
        self.ages = np.array(self.ages)
        self.genders = np.array(self.genders)
        return self.images, self.genders, self.ages
        
