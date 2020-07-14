import heapq
import math
import numpy as np
import re
import os

biography_dataset = []

#load text from data file
def load_text():
    path = os.path.join(os.path.dirname(__file__), 'biography.txt')
    file = open(path, 'r')

    Lines = file.readlines()
    one_biography = ""
    i = 0
    condition = 0
    while i < len(Lines):
        if "-lrb-" in Lines[i]:
            if condition == 0:
                one_biography = Lines[i]
                condition = 1
            else:
                biography_dataset.append(one_biography)
                one_biography = Lines[i]
        else:
            one_biography += Lines[i]
        i += 1

    #Close the file
    file.close()

#Convert the letters into lower case, remove symbols for the strings saved in the dataset
def text_processing(dataset):
    for i in range(len(dataset)):
        dataset[i] = dataset[i].lower()
        dataset[i] = re.sub(r'\W', ' ', dataset[i])
        dataset[i] = re.sub(r'\s+', ' ', dataset[i])
    return dataset

load_text()
biography_dataset = text_processing(biography_dataset)
