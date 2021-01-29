#Author Nicholas Mosca
# Description hw0 problem 1

#parse and preprocess data
#no pandas
#load data in
# loop through each line
#convert to string
# replace ? with NaN
#loop based on , split 
# convert all to float

import math

def import_data(filename):
    ''' parsing .data file''' 
    file = open(filename, 'r')
    #nested list
    X = []
    #last element of each row
    y = []
    #counting attributes
    count = 0
    # cleaning each row
    data = file.readlines()
    for line in data:
        line = line.split(',')
        
        for element in line:
            count +=1
            if element == "?":
                #converting to float
                element = float('NaN')
            else:
                element = float(element)
            if element == '-':
                element = element.strip('-')
            if count != 280:
                X.append(element)
            if count == 280:
                y.append(element)
                count = 0
            
        # need to add 279 then restart
    return X, y
                
        
            
    
    
        
             
 
import_data('arrhythmia.data')
    
   



