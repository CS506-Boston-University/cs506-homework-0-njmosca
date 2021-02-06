#Problem 4 hw0
#Author: Nicholas Mosca

#import non numerical data

test = ['548', '2', 'male', '', '0', '0', '13.8625', 'C']
#convert str to int and 
    # convert floats
    # missing = float('nan')
   # helper function input = list
    # if blank replace float nan
 #gender female = 0, male = 1
# embarked C = 0, Q = 1, S = 2 
def convert(l):
    ''' converts strings to floats'''
    new_list = []
    for element in l:
        if element == 'female':
            new_list.append(int(0))
        elif element == 'male':
            new_list.append(int(1))
        elif element == 'C':
            new_list.append(int(0))
        elif element == 'Q':
            new_list.append(int(1))
        elif element == 'S':
            new_list.append(int(2))
        elif element == "":
                #converting to float
                element = float('NaN')
        else:
            new_list.append(float(element))
    return new_list


def import_data2(file):
    ''' imports data thats multiple data types
    returns y = survived feature that will be numerical
    returns X thats the remaining features'''
   

    file = open(file, 'r')
    X = []
    y = []
    
    data = file.readlines()
    for line in data[1:]:
        temp = []
        q1 = line.find('"') # first quote
        q2 = line.rfind('"') # last quote
        
        row_entries1 = line[0:q1].strip(',').split(',')
        row_entries2 = line[q2+1:].strip(',').split(',')
        
        temp.append(row_entries1[0])
        temp.append(row_entries1[2])
        temp.append(row_entries2[0])
        temp.append(row_entries2[1])
        temp.append(row_entries2[2])
        temp.append(row_entries2[3])
        temp.append(row_entries2[5])
        temp.append(row_entries2[7].strip('\n'))

        # appending survived list from second column
        y.append(row_entries1[1])
        X.append(temp)
        new_X = []
    for l in X:
        new_X.append(convert(l))
    import pdb; pdb.set_trace()
    
    return new_X , y

    
            

   


