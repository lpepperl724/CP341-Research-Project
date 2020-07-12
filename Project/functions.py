#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program stores the functions needed for 
the page generator.

"""
import skimage
from skimage import io
import random,string,requests,os,datetime
from skimage.transform import resize
import numpy as np
import pandas as pd


# given any list, this function randomly picks an element out of the list 
def randomPicker(input_list):
    this_item = input_list[random.randint(0,len(input_list)-1)]
    return this_item

def nameGenerator():
    
    # generates the first and last names for the person
    # we use gender-neutral first names from https://nameberry.com/unisex-names
    # and the 50 most popular last names in U.S.

    first_names = ['Avery','Riley','Jordan','Angel','Parker','Sawyer','Peyton','Quinn','Blake','Hayden','Taylor','Alexis','Rowan','Charlie','Emerson','Finley','River','Ariel','Emery','Morgan','Elliot','London','Eden','Elliott','Karter','Dakota','Reese','Zion','Remington','Payton','Amari','Phoenix','Kendall','Harley','Rylan','Marley','Dallas','Skyler','Spencer','Sage','Kyrie','Lyric','Ellis','Rory','Remi','Justice','Ali','Haven','Tatum','Kamryn']
    this_first_name = randomPicker(first_names) + ' '

    
    last_names = ['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez','Martinez','Hernandez','Lopez','Gonzalez','Wilson','Anderson','Thomas','Taylor','Moore','Jackson','Martin','Lee','Perez','Thompson','White','Harris','Sanchez','Clark','Ramirez','Lewis','Robinson','Walker','Young','Allen','King','Wright','Scott','Torres','Nguyen','Hill','Flores','Green','Adams','Nelson','Baker','Hall','Rivera','Campbell','Mitchell','Carter','Roberts']
    this_last_name = randomPicker(last_names)

    # determine if middle name will be generated
    # if i = 1, then a middle name will be added
    i = random.randint(0,1)
    
    if i == 1:
        middle_name = list(string.ascii_uppercase)[random.randint(0,25)] + '. ' 
        name = this_first_name + middle_name + this_last_name
    else:
        name = this_first_name + this_last_name

    return(name)

# this code is adapted from https://stackoverflow.com/questions/50559078/generating-random-dates-within-a-given-range-in-pandas
def dateGenerator(unit='D', seed=None):
    # the year of birth needs approx. age
    # and will be added later
    start = pd.to_datetime('1970-01-01')
    end = pd.to_datetime('2020-01-01')

    if not seed:  # from piR's answer
        np.random.seed(0)

    ndays = (end - start).days + 1
    raw_date = start + pd.to_timedelta(
        np.random.randint(0, ndays, 1), unit=unit
    )
    raw_date = str(list(raw_date)[0])
    date = raw_date[0:raw_date.find(' ')]
    return date

# generates a random place
# from the 1000 most populated cities
# in US
def placeGenerator():
    # data from https://gist.github.com/Miserlou/11500b2345d3fe850c92
    fhand = open('cities.txt')

    # split the data
    raw_data = [x.split(',') for x in fhand.readlines()]
    
    # delete the header
    del raw_data[0:14]
    
    this_place = randomPicker(raw_data)
    
    return this_place[1] + ', ' + this_place[2]

#fetches images from the website 
#'thispersondoesnotexist.com'

def getImage():    
    
    image_url = 'http://thispersondoesnotexist.com/image'
    
    img_data = requests.get(image_url).content
    
    # save the image
    with open('static/img/profile_image.jpg', 'wb') as handler:
        handler.write(img_data)
        
    # get and resize the image
    my_image = io.imread('static/img/profile_image.jpg')
    my_image = resize(my_image, (220, 220))
    
    # resave the image
    io.imsave('static/img/image_resized.jpg', my_image)
