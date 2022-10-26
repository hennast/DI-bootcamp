import numpy as np
import pandas as pd

#Write a function to create a numpy array using only the input: start, length, and stop.
#Use the function to create an numpy array of length 100, starting from 6 and has a step of 4 between consecutive numbers

a = np.linspace(6, 402, 100)

#2
b = np.array([1,2,3,np.nan,5,6,7,np.nan])
new_array = b[np.logical_not(np.isnan(b))]

#3
#create a random numpy array that has a shape of (5, 6) filled with integers between 1 and 100.
#Then compute the maximum int for each row in the array
c = np.random.randint(1,100, size = (5,6))
print(c)

max_int = np.amax(c, axis=1)
print(max_int)


