'''from keras.layers import Input, Dense, Reshape, FLatten, Dropout, \
    BatchNormalization, Activation, ZeroPadding2D
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Sequential, Model
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import numpy as np'''

#hyperparameters
epochs = 0
batch_size = 0
save_interval = 0


class GAN():
    def __init__(self):
        #input shape
        return
    
    def generator(self):
        #Input -> img
        #Output -> img + labels (age & gender)
        return
    
    def discriminator(self):
        #Input -> img + labels (age & gender)
        #Output -> real/fake classification
        return
    
    def train(self):
        #train discriminator to correctly classify generator      
        #train generator to fool discriminator     
        #repeat for num epochs
        return
    

def getData():
    return


if __name__ == '__main__':
    True