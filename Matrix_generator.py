import numpy as np
import random


def func(amount,number,x_axis,y_axis):
    arr = []
    while len(arr) < amount:
        x = random.randrange(number)
        arr.append(x)
        
    new_arr = np.array(arr)
    new_arr.shape = (x_axis,y_axis)
    return new_arr

print(func(10,2,2,5))