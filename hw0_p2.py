#Author Nicholas Mosca 
#CS506
#Impute or delete missing entries
import math
from hw0_p1 import import_data


X, y = import_data('arrhythmia.data')
# used to test functions
#test = [[float('nan'),2,3,4],[1,2,3,float('nan')],[2,2,4,5],[1,2,5,6,]]
#testy = [0,1,2,3]
#Helper Functions

def transpose(x):
    ''' transposes nested list, Row--> col'''
    t_list = list(map(list,zip(*x)))
    return t_list

#takes median of single list
def median(x):
    ''' x = list'''
    n = len(x)
    s = sorted(x)
    return (sum(s[n//2-1:n//2+1])/2.0,s[n//2])[n%2] if n else None

def remove_nan(l):
    #creates empty list same size
    new_list = [[]] * len(l)
    for i in range(len(l)):
        new_list[i] = [x for x in l[i] if math.isnan(x) == False]
    return new_list

def replace_nan(l,value):
    ''' l = list, replace all nan in list l with value'''
    new_list = []
    for i in range(len(l)):
        if math.isnan(l[i]):
            new_list.append(value)
        else:
            new_list.append(l[i])

    return new_list
            

#2a
def impute_missing(X):
    ''' remove NaN and compute median'''
    #transpose X
    trans_x = transpose(X)
    new_list = [[]] * len(trans_x)
    #remove NaN
    cleaned_trans_x = remove_nan(trans_x)
    #find medians
    med_list = []
    #loop through cleaned transposed x
    for feature in cleaned_trans_x:
        #import pdb; pdb.set_trace()
        med_list.append(median(feature))
    #loop through regular
    index = 0
    #debug code
    #import pdb; pdb.set_trace()
    for x in trans_x:
        #import pdb; pdb.set_trace()
        #print(new_list[0],x,med_list[0] )
        new_list[index] = replace_nan(x,med_list[index]) 
        index += 1     
    return transpose(new_list)

new_X = impute_missing(X)

#2b
'''2b---> Median can be a useful tool instead of mean for a few reasons. Mean or average 
includes all outlier/ extreme points that do not represent most of the dataset. Median is the middle or 
representation of a datapoint in the middle of the set. Using median reduces the change of
skewing the data.'''


#2c
# Helper function

def has_nan(X):
    ''' scans row for nan values in single list
    returns True or False
    1 = True
    2 = False'''
    results = []
    for element in X:
        if math.isnan(element):
            results.append(True)
        else:
            results.append(False)
    return any(results)
    
        
# write function that discards missing values of from dataset
def discard_missing(X,y):
    ''' X = attribute, y = patient class
    if nan in list of attributes, remove that attribute list and patient class'''
    new_X = []
    new_y = []
    #tests
    old_X =[]
    old_y = []
    for row in range(len(X)):
        if has_nan(X[row]) == False:
            new_X.append(X[row])
            new_y.append(y[row])
        else:
            old_X.append(X[row])
            old_y.append(y[row])

    return new_X, new_y, old_X,old_y


clean_x, clean_y, dirty_x,dirty_y = discard_missing(X,y)   

  
