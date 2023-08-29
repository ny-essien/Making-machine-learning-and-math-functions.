def accuracy_score(y_true,y_pred):
    stacks = []
    if type(x) != list:
        raise TypeError('x must be a list')
    
    if (len(y_true) != len(y_pred)):
        raise AttributeError("Length of y_pred must be same as y_tru")
        
    for i in range(0, len(y_pred)):
        if (y_true[i] == y_pred[i]):
            stacks.append(i)
    accuracy = (len(stacks)/len(y_true))
    pecentage = accuracy * 100 
    return " %.2f " % pecentage +"%"


def scaler_multiplication(x,mulitplier):

    sca_mul = []
    if type(x) != list:
        raise TypeError('x must be of type list')
    
    for i in x:
        sca_mul.append(i * mulitplier)
    
    return sca_mul

def sum_num(x):

    start = 0
    if not isinstance(x, (list, tuple)):
        raise TypeError('Invalid type. x must be either a list or a tuple')
    for val in x:
        start += val
    return start

def mean_val(x):

    num_of_elements = len(x)
    if not isinstance(x, (list,tuple)):
        raise TypeError('Invalid type. x must be either a list or a tuple')
    return (sum_num(x)/num_of_elements)
    
def min_value(x):

    if not isinstance(x, (list, tuple)):
        raise TypeError('Invalid type. x must be either a list or a tuple')
    stacks = []
    for i in range(len(x)):
        for val in x:
            if x[i] == val:
                continue
            if x[i] < val:
                stacks.append('*')
        if len(stacks) != (len(x) - 1):
            stacks.clear()
        else:
            return x[i]
        
def max_value(x):

    if not isinstance(x, (list,tuple)):
        raise TypeError('Invalid type. x must be either a list or a tuple')
    
    stacks = []
    for i in range(len(x)):
        for val in x :
            if x[i] == val:
                continue
            if x[i] > val:
                stacks.append('*')
        if len(stacks) != (len(x) - 1):
            stacks.clear()
        else:
            return x[i]
        
def square_root(x):
    if not isinstance(x, (list, tuple, list, float)):
        raise TypeError('invalid type')
    
    if isinstance(x, (list, tuple)):
        new_list = []
        for val in x:
            new_list.append(val ** 0.5)
        if len(new_list) == 1:
            return float(new_list[0])
        return new_list
    
    return x**0.5

def absolute_value(x):

    if not isinstance(x, (list, tuple, int, float)):
        raise TypeError('invalid type')
    
    if isinstance(x,(list, tuple)):

        for i in range(len(x)):
            if x[i] > 0:
                continue
            if x[i] < 0:
                x[i] = -1 * x[i]
        return x
    
    if isinstance(x, (int, float)):
        if x > 0:
            return x
        
        return -1 * x
   
def standard_deviation(x):

    x_mean = mean_val(x)
    num_of_elements = len(x)
    stacks = []
    if not isinstance(x, (list, tuple)):
        raise TypeError('Invalid type. x must be either a list or a tuple')
    for i in x:
        mxl = ((i - x_mean)**2/num_of_elements)
        stacks.append(mxl)
    summation = [sum_num(stacks)]

    return square_root(summation)

def normalization(x):

    norm = []
    x_min = min_value(x)
    x_max = max_value(x)
    if not isinstance(x, (list,tuple)):
        raise('Invalid type. x must be either a list or a tuple')
    for val in x:
        normalised_val = ((val - x_min)/(x_max - x_min))
        norm.append(normalised_val)

    return norm

def standardization(x):
    
    norm = []
    x_mean = mean_val(x)
    std = standard_deviation(x) 

    if not isinstance(x, (list,tuple)):
        raise('Invalid type. x must be either a list or a tuple')
    for val in x:
        stadardised_data = ((val - x_mean)/std)
        norm.append(stadardised_data)
    
    return norm

if __name__ == "__main__":

    #y_true = [0,1,1,0,0,1]
    #y_pred = [0,1,1,0,0,1]

    #print(accuracy_score(y_true, y_pred))
    #print(scaler_multiplication([1,2,3],3))

    x = (400,140,56,1000,100,46)
    print(min_value(x))
    print(max_value(x))
    print(normalization(x))
    print(standardization(x))
    print(sum(x))
    print(mean_val(x))
    print(square_root(x))
    print(standard_deviation(x))
    print(square_root(x))
    print(absolute_value([2,-3,4,-5]))




