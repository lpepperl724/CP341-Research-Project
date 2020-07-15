from keras.models import Model, load_model
from keras.layers import Input, Dropout, ZeroPadding2D, BatchNormalization, Dense, Flatten
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import Conv2D
from sklearn.model_selection import KFold
from os.path import isdir
import random
import numpy as np

class MultiOutputModel:
    def __init__(self, rows, cols, channels=3, mpath='model', load=False):
        self.mpath=mpath
        self.img_shape = (rows, cols, channels)       
        if load and isdir(self.mpath):
            self.m = load_model(self.mpath)
        else:
            self.build()

    def build(self):
        i = Input(shape=self.img_shape)
        x = Conv2D(32, kernel_size=3, strides=2, padding='same', input_shape=self.img_shape)(i)
        x = LeakyReLU()(x)
        x = Dropout(.25)(x)
        x = Conv2D(64, 3, 2, 'same')(x)
        x = ZeroPadding2D(((0,1), (0,1)))(x)
        x = BatchNormalization(momentum=.8)(x)
        x = LeakyReLU()(x)
        x = Dropout(.25)(x)
        x = Conv2D(128, 3, 2, 'same')(x)
        x = BatchNormalization(momentum=.8)(x)
        x = LeakyReLU()(x)
        x = Dropout(.25)(x)
        x = Flatten()(x)
        o1 = Dense(1, activation='sigmoid')(x) # gender
        o2 = Dense(1, activation='relu')(x) # age
        
        self.m = Model(i, [o1, o2])
        self.m.compile(optimizer='adam', loss=['binary_crossentropy', 'mean_squared_error'], metrics=['accuracy', 'MeanSquaredError'])
    
        
    def train(self, X, y0, y1, e):
        self.m.fit(X, [y0, y1], epochs=e, batch_size=10)
        self.m.save(self.mpath)
    
    def test(self, X, y0, y1):
        self.m.evaluate(X, [y0, y1], batch_size=10)
    
    def predict(self, x):
        return self.m.predict(np.array([x,]))