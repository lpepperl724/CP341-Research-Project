# module imports
from Dataset_Creator import Dataset_Creator
from multioutputmodel import MultiOutputModel
from imager_fetcher import ImageFetcher

#library imports
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

'''
Parameters:
dc_folder - location of the training dataset (if not load_model)
img_width - resize width of all images
img_height - resize height of all images
max_data - maximum amount of data loaded for training/testing (if not load_model)
load_model - if True: load previously trained model from 'model' folder, if False: build and trian new model
epochs - number of training epochs per trial (if not load_model)
trials - number of training sessions using unique subsets of the data (if not load_model)
image_saveloc - location to save prediction image
'''
dc_folder = 'part1/'
img_width = 150
img_height = 150
max_data = 1000
load_model = False
epochs = 20
trials = 5
image_saveloc = 'prediction.png'


def main():
    # initialize our model
    print("Initializing model..")
    MOM = MultiOutputModel(img_width, img_height, load=load_model)
    
    if load_model == False:
        # get the dataset for training our model
        print("Loading dataset..")
        DC = Dataset_Creator()
        images, genders, ages = DC.getData(dc_folder, img_width, img_height, max_data)
        
        # train/test the model
        print("Training model..")
        for t in range (trials):
            X_train, X_test, y0_train, y0_test, y1_train, y1_test = train_test_split(images, genders, ages, test_size=.2)
            MOM.train(X_train, y0_train, y1_train, epochs)
        #print("Testing model..")
        #print(MOM.test(X_test, y0_test, y1_test))
       
    # create some fake data
    print("Generating fake data..")
    IF = ImageFetcher()
    image = IF.getImage('http://thispersondoesnotexist.com/image', image_saveloc, img_width, img_height)
    p = MOM.predict(image)
    gender = round(p[0][0][0])
    age = round(p[1][0][0])
    
    #display results
    plt.imshow(image, interpolation='nearest')
    plt.axis('off')
    plt.show()
    print("PREDICTION:  gender: %d  age: %d" % (gender, age))
    
    # generate a biography
    print("Building biography..")
    #bio(image, gender, age)

if __name__ == '__main__':
    main()
    
    
    
        
    
    











