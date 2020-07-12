import numpy as np
import cv2
from sklearn.model_selection import KFold
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization, ZeroPadding2D
from keras.layers.convolutional import Conv2D
from keras.layers.advanced_activations import LeakyReLU

class ImgModel:
    def __init__(self, rows=180, cols=180, channels=1, latent_dim=100):
        self.img_shape = (rows, cols, channels)
    
    def genderClassifier(self):
        self.model = Sequential()       
        self.model.add(Conv2D(32, kernal_size=3, strides=2, input_shape=self.img_shape, padding='same'))
        self.model.add(LeakyReLU(alpha=.2))
        self.model.add(Dropout(.25))
        self.model.add(Conv2D(64, kernal_size=3, strides=2, padding='same'))
        self.model.add(ZeroPadding2D(padding=((0,1),(0,1))))
        self.model.add(BatchNormalization(momentum=.8))
        self.model.add(LeakyReLU(alpha=.2))
        self.model.add(Dropout(.25))
        self.model.add(Conv2D(128, kernal_size=3, strides=2, padding='same'))
        self.model.add(BatchNormalization(momentum=.8))
        self.model.add(LeakyReLU(alpha=.2))
        self.model.add(Dropout(.25))
        self.model.add(Flatten())
        self.model.add(Dense(1, activation='sigmoid'))   
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.model.summary()        
        #img = Input(shape=self.img_shape)
        #validity = model(img)
        #return Model(img, validity)
    
    def train(self, X, y, e, bs, si=0):
        self.model.fit(X, y, batch_size=bs, epochs=e, verbose=0)
    
    def test(self, X, y, bs):
        return self.model.evaluate(X, y, batch_size=bs, verbose=0)
    
    def saveModel(self):
        return

def getData():
    data = []
    labels = []
    return data, labels

def main():
    X, y = getData()
    #train_test_ratio = .8
    #train_index = random.sample(range(len(X)))
    #test_index = [x for x in range(0, len(X)) if x not in train_index]
    M = ImgModel()
    M.genderClassifier()
    kf = KFold(n_splits=10)
    i = 0
    for train_index, test_index in kf.split(X):
        i += 1
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        M.train(X=X_train, Y=y_train, e=200, bs=32, si=10)
        loss, accuracy = M.test(X_test, y_test)
        print("Fold %d results:  loss=%.3f  accuracy=%.3f" % (i, loss, accuracy))
    