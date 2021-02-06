# Problem 3 hw0
#Author: Nicholas Mosca

import math
from hw0_p1 import import_data
from hw0_p2 import *
import numpy as np
import random
import math


#3a
#create function that shuffles data in both X and y
# shuffle X then match y? or shuffle both?
#create random list size of input ( numpy array) 0 - 67
# new list of indexs
#set index of empty list to the 

def shuffle_data(X, y):
    ''' shuffles both X and Y''' 
    random_list = np.array(range(len(X)))
    np.random.shuffle(random_list)
    new_X = []
    new_y = []
    for i in random_list:
        new_X.append(X[i])
        new_y.append(y[i])
    return X, y

#3b
# transpose X 
# calculate std
# flip back
def std_row(row):
    ''' computes std of a entire row'''
    mean=sum(row)/len(row)
    std = (sum( (x-mean)**2.0 for x in row ) / float(len(row)) )**0.5
    return std

def compute_std(X):
    ''' computes std for each column, returns list of stds'''
    std_list = []
    X = transpose(X)
    for l in X:
        std_list.append(std_row(l))
    return std_list
        

#3c
#transpose
#function that removes features that are not within two std of mean of a given feature(row)
#compute std for each row, remove enties within 2 std of mean of

def mean(l):
    ''' calculates mean of  list'''
    mean = sum(l)/len(l)
    return mean

def remove_outlier( X, y):
    ''' removes value that is more than 2 std away from mean'''
    X = transpose(X)
    keepers = []
    new_X = [[]] * len(X)
    ol = [[]] * len(X)
    new_y = []
    oly = []
    for feature in X:
        feature_mean = mean(feature)
        feature_std = std_row(feature)
        compare_value1 = abs(feature_mean + (2* feature_std))
        compare_value2 = abs(feature_mean - (2* feature_std))
        
        for value in feature: 
            if abs(value) > abs(compare_value1) or abs(value) < abs(compare_value2):
                ol.append(value)
            else:
                keepers.append(value)
        new_X.append(keepers)
        keepers = []
    #import pdb; pdb.set_trace()
                
    # have to do the same for y?
    # y is 1-16 and should stay same length as len(X) would not want to delete?
    for value in y:
        y_mean = mean(y)
        std_y = std_row(y)
        high = y_mean + 2 * std_y
        low = y_mean - 2* std_y
        if abs(value) > abs(high) or abs(value) < abs(low):
            oly.append(value)
        else:
            new_y.append(value)

    return new_X ,new_y


    

#3d
#transpose
# helper function that takes value - mean // std of list  (x to x prime)
