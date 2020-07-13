from keras.models import Model, load_model
from keras.layers import *
from sklearn.model_selection import KFold
from os.path import isfile

class MultiOutputModel:
    def __init__(self, mpath='model.model', load=False, rows, cols, channels=1):
        self.img_shape = (rows, cols, channels)       
        if isfile(mpath) and load:
            print("Loading existing model")
            self.m = load_model(mpath)
        else:
            print("Building new model")
            self.build()

    def build(self):
        i = Input(shape=self.img_shape)
        x = Conv2D(32, kernal_size=3, strides=2, padding='same', input_shape=self.img_shape)(i)
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
        self.m.compile(optimizer='adam', loss=['binary_crossentropy', 'mean_squred_error'], metrics='accuracy')
    
    def train(self, X, y, e, bs):
        self.m.fit(X, [y[0], y[1]], epochs=e, batch_size=bs)
        self.m.save()
    
    def test(self, X, y, bs):
        return self.m.evauluate(X, [y[0], y[1]], batch_size=bs, verbose=0)
    
    def predict(self, x):
        return self.m.predict(x)

def getData():
    return

def main():
    X, y = getData()
    
    M = MultiOutputModel()
    kf = KFold(n_splits=10)
    i = 0
    for train_index, test_index in kf.split(X):
        i += 1
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        M.train(X=X_train, Y=y_train, e=200, bs=32, si=10)
        loss, accuracy = M.test(X_test, y_test)
        print("Fold %d results:  loss=%.3f  accuracy=%.3f" % (i, loss, accuracy))