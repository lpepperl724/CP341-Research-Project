from __future__ import print_function

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.utils.data_utils import get_file
from keras.models import model_from_json
import numpy as np
import random
import sys
import os
import collections


path = "output.txt"

text = open(path).read().lower()

print('corpus length:', len(text))

chars = set(text)
words = open('output.txt').read().lower().split()

i=0
# Delete words that are too uncommon
counter=collections.Counter(words)
for value in counter.values():
    if value >= 3:
        i+= 1

new_words = []
for pair in counter.most_common(i):
    new_words.append(pair[0])
    
words = set(words)

print("words",type(words))
print("total number of unique words",len(words))
print("total number of common words",len(new_words))

word_indices = dict((c, i) for i, c in enumerate(new_words))
indices_word = dict((i, c) for i, c in enumerate(new_words))

print("word_indices", type(word_indices), "length:",len(word_indices))
print("indices_words", type(indices_word), "length", len(indices_word))

maxlen = 30
step = 3
print("maxlen:",maxlen,"step:", step)
    
sentences = []
next_words = []
next_words= []
list_words = []

sentences2=[]

print('Cleaning the sentences...')

list_words = text.lower().split()

list_words = [word for word in list_words if word in new_words]

for i in range(0,len(list_words)-maxlen, step):
    sentences2 = ' '.join(list_words[i: i + maxlen])
    sentences.append(sentences2)
    next_words.append((list_words[i + maxlen]))
    
print('number of sentences in the dataset:', len(sentences))
'''
for i in range(0,len(sentences)):
    if (i % 5000 = 0):
        print ('The sentence ' + str(i) + ' have been cleaned.')
    sentence = sentences[i].split(' ')
    sentence = [word for word in sentence if word in new_words]
    sentences[i] = ' '.join(sentence)
'''    
print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(new_words)), dtype=np.bool)
y = np.zeros((len(sentences), len(new_words)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, word in enumerate(sentence.split()):
        #print(i,t,word)
        X[i, t, word_indices[word]] = 1
    y[i, word_indices[next_words[i]]] = 1

'''
#build the model: 2 stacked LSTM
print('Build model...')
model = Sequential()
model.add(Dense(len(new_words)))
model.add(LSTM(70, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(70, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(len(new_words)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')
'''
def sample(a, temperature=1.0):
    # helper function to sample an index from a probability array
    a = a / np.sum(a)
    print('a is' + str(np.sum(a)))
    return np.argmax(np.random.multinomial(1, a, 1))

def bioGenerator():
# train the model, output generated text after each iteration
    #Load the data
    path = "output.txt"

    text = open(path).read().lower()
    
    print('corpus length:', len(text))
    
    chars = set(text)
    words = open('output.txt').read().lower().split()
    
    i=0
    # Delete words that are too uncommon
    counter=collections.Counter(words)
    for value in counter.values():
        if value >= 3:
            i+= 1
    
    new_words = []
    for pair in counter.most_common(i):
        new_words.append(pair[0])
        
    words = set(words)
    
    print("words",type(words))
    print("total number of unique words",len(words))
    print("total number of common words",len(new_words))
    
    word_indices = dict((c, i) for i, c in enumerate(new_words))
    indices_word = dict((i, c) for i, c in enumerate(new_words))
    
    print("word_indices", type(word_indices), "length:",len(word_indices))
    print("indices_words", type(indices_word), "length", len(indices_word))
    
    maxlen = 30
    step = 3
    print("maxlen:",maxlen,"step:", step)
        
    sentences = []
    next_words = []
    next_words= []
    list_words = []
    
    sentences2=[]
    
    print('Cleaning the sentences...')
    
    list_words = text.lower().split()
    
    list_words = [word for word in list_words if word in new_words]
    
    for i in range(0,len(list_words)-maxlen, step):
        sentences2 = ' '.join(list_words[i: i + maxlen])
        sentences.append(sentences2)
        next_words.append((list_words[i + maxlen]))
        
    print('number of sentences in the dataset:', len(sentences))
    '''
    for i in range(0,len(sentences)):
        if (i % 5000 = 0):
            print ('The sentence ' + str(i) + ' have been cleaned.')
        sentence = sentences[i].split(' ')
        sentence = [word for word in sentence if word in new_words]
        sentences[i] = ' '.join(sentence)
    '''    
    print('Vectorization...')
    X = np.zeros((len(sentences), maxlen, len(new_words)), dtype=np.bool)
    y = np.zeros((len(sentences), len(new_words)), dtype=np.bool)
    for i, sentence in enumerate(sentences):
        for t, word in enumerate(sentence.split()):
            #print(i,t,word)
            X[i, t, word_indices[word]] = 1
        y[i, word_indices[next_words[i]]] = 1
        
    # Load the model
        
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights('model.h5')
    
    model = loaded_model
    
    fake_bio = []
    for iteration in range(0, 5):
        print()
        print('-' * 50)
        print('Iteration', iteration)
        model.fit(X, y, batch_size=512, epochs=1)
        model.save_weights('GoTweights',overwrite=True)
    
        start_index = random.randint(0, len(list_words) - maxlen - 1)
    
        for diversity in [0.2, 0.5, 1.0, 1.2]:
            print()
            generated = ''
            sentence = list_words[start_index: start_index + maxlen]
            generated += ' '.join(sentence)
            print('----- Generating with seed: "' , sentence , '"')
            print()
            sys.stdout.write(generated)
            print()
    
            for i in range(300):
                x = np.zeros((1, maxlen, len(words)))
                for t, word in enumerate(sentence):
                    x[0, t, word_indices[word]] = 1.
    
                preds = model.predict(x, verbose=0)[0]
                #print(preds)
                #print(type(preds))s
                #print(diversity)
                #print(type(diversity))
                
                next_index = sample(preds)
                next_word = indices_word[next_index]
                generated += next_word
                del sentence[0]
                sentence.append(next_word)
                sys.stdout.write(' ')
                sys.stdout.write(next_word)
                sys.stdout.flush()
            print()
        
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")

model.save_weights('weights') 