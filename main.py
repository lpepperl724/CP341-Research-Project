# module imports
from Dataset_Creator import Dataset_Creator
from multioutputmodel import MultiOutputModel
from imager_fetcher import ImageFetcher

#library imports
from sklearn.model_selection import KFold
'''
'''
dc_folder = 'part1/'
img_width = 150
img_height = 150
max_data = 500
load_model=True
epochs = 50
folds = 10
image_saveloc = ''


def main():
    # initialize our model
    MOM = MultiOutputModel(img_width, img_height, load_model)
    
    # get the dataset for training our model
    if load_model == False:
        DC = Dataset_Creator()
        images, genders, ages = DC.getData(dc_folder, img_width, img_height, max_data)
    
        # train/test the model
        MOM.train(images, genders, ages, epochs)
        #MOM.test()
       
    # create some fake data    
    IF = ImageFetcher()
    image = IF.getImage('http://thispersondoesnotexist.com/image', image_saveloc, img_width, img_height)
    gender, age = MOM.predict(image)
    
    # generate a biography
    #bio(image, gender, age)
    
    
    
        
    
    











