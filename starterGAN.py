from keras.layers import Input, Dense, Reshape, Flatten, Dropout, \
    BatchNormalization, Activation, ZeroPadding2D
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import Conv2D
from keras.models import Sequential, Model

#hyperparameters
epochs = 0
batch_size = 0
save_interval = 0


class GAN():
    def __init__(self):
        #input shape 
        self.input_shape = (64, 64, 3) #64x64 RGB
        return
    
    def generator(self):
        #Input -> img
        #Output -> img + labels (age & gender)
        
        model = Sequential()
        model.add(Conv2D(input_shape=self.input_shape))
        return
    
    def discriminator(self):
        #Input -> img + labels (age & gender)
        #Output -> real/fake classification
        
        model = Sequential()
        model.add(Conv2D(filters=32, input_shape=self.input_shape))
        model.add(LeakyReLU())
        model.add(Dropout(0.25))
        model.add(Conv2D(filters=62))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Flatten())
        model.add(Dense(units=2))
        
        model.summary()
        img = Input(shape=self.img_shape)
        validity = model(img)

        return Model(img, validity)         
    
    def train(self, e, bs, si):
        for epoch in range(e):
            # ---------------------
            #  Train Discriminator
            # ---------------------
            
            #1. select random training set      
            #2. generate new image/label pairings
            #3. train discriminator on classified data
            
            # ---------------------
            #  Train Generator
            # ---------------------
            
            #train generator
            
            return
    

def getData():
    return


if __name__ == '__main__':
    g = GAN()
    g.train(epochs, batch_size, save_interval)