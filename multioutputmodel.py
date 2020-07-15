from keras.models import Model, load_model
from keras.layers import *
from sklearn.model_selection import KFold
from os.path import isfile
import random
from Dataset_Creator import Dataset_Creator
import numpy as np
import matplotlib.pyplot as plt

class MultiOutputModel:
    def __init__(self, rows, cols, channels=3, mpath='model.model', load=False):
        self.img_shape = (rows, cols, channels)       
        if load and isfile(mpath):
            print("Loading existing model")
            self.m = load_model(mpath)
        else:
            print("Building new model")
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
    
        
    def train(self, X, y0, y1, e, bs):
        self.m.fit(X, [y0, y1], epochs=e, batch_size=bs)
        self.m.save('model.model')
    
    def test(self, X, y0, y1, bs):
        return self.m.evaluate(X, [y0, y1], batch_size=bs, verbose=0)
    
    def predict(self, x):
        return self.m.predict(np.array([x,]))

def getData():
    DC = Dataset_Creator()
    images, genders, ages = DC.getData('part1/', 100, 100)
    return images, genders, ages

def main():
    print("Getting data..")
    X, y0, y1 = getData()
    M = MultiOutputModel(100, 100)
    
    ratio=1
    if ratio != 1:
        reduced_index = random.sample(range(len(X)), int(ratio * len(X)))
        X = X[reduced_index]
    
    kf = KFold(n_splits=10)
    i = 0 
    print("Training/Testing..")
    for train_index, test_index in kf.split(X):
        i += 1
        X_train, X_test = X[train_index], X[test_index]
        y0_train, y0_test = y0[train_index], y0[test_index]
        y1_train, y1_test = y1[train_index], y1[test_index]
        M.train(X_train, y0_train, y1_train, e=50, bs=32)
        M.test(X_test, y0_test, y1_test, bs=32)
        #loss, accuracy = M.test(X_test, y0_test, y1_test, bs=32)
        #print("Fold %d results:  loss=%.3f  accuracy=%.3f" % (i, loss, accuracy))
        print('PREDICTION:', M.predict(X_test[0]))
        print('ACTUAL:', y0_test[0], y1_test[0])
        plt.imshow(X_test[0], interpolation='nearest')
        plt.show()

main()