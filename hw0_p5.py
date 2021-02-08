#HW0 problem 5
#Author: Nicholas Mosca
# going to shuffle and split dataset according to fractions (0-1)
import numpy as np
import math
from hw0_p2 import clean_x
from hw0_p2 import clean_y
from hw0_p3 import shuffle_data

test = np.arange(0,10)
test2d = np.arange(50).reshape(10, 5)
#5A
def train_test_split(X, y, t_f):
    ''' splits one dataset into training and testing sets t_f = test set %'''
    X = np.array(X)
    y = np.array(y)
    #splitting X
    split_x = np.split(X,[int(t_f * len(X))]) 
    #splitting y
    split_y = np.split(y,[int(t_f * len(y))]) 
    # shuffle
    split_x,split_y = shuffle_data(split_x,split_y)
    # assigning segments
    x_train = split_x[1]
    x_test = split_x[0]
    y_train = split_y[1]
    y_test = split_y[0]
    
    return x_train, y_train, x_test, y_test


#5B
#split data like 5A but creates a cv_f set or cross validation fraction
# all sets must add to 100% of total data

def train_test_CV_split(X,y, t_f, cv_f):
    ''' takes datasets X,y returns test, train and validation set that can be a overlap'''
    X = np.array(X)
    y = np.array(y)
    #splitting x and y
    split_x = np.split(X,[int(t_f * len(X))]) 
    split_y = np.split(y,[int(t_f * len(y))]) 
     # shuffle
    split_x,split_y = shuffle_data(split_x,split_y)
    # x testing
    x_test = split_x[0] # test set
    #creating validation set and train set
    valid = np.split(split_x[1],[int(cv_f * len(split_x[1]))]) # takes % of leftover for validation set
    # x validation
    x_valid = valid[1]
    # x train
    x_train = valid[0]
    #import pdb; pdb.set_trace()
    # y test
    y_test = split_y[0] # test set
    valid_y = np.split(split_y[1],[int(cv_f * len(split_y[1]))])
    # y validation
    y_valid = valid_y[1]
    # x train
    y_train = valid_y[0]

    return x_train, y_train, x_test, y_test, x_valid, y_valid









