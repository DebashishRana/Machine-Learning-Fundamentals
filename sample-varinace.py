import numpy as np
import statistics as stat 
import math 

def sample_var_std(x: list | np.array ,n:int) -> float:
    """ Calculating sample variance  """
    mean = stat.mean(x)
    difference_list = []
    for y in x:
        diff = mean - x
        difference_list.append(diff)
    s = sum(difference_list)
    numerator = math.square(s)
    main = numerator/n-1
    return main




