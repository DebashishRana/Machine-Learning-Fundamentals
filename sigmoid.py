import numpy as np
import math 

def sigmoid(x: list, y:list,b:float) -> np.ndarray | float:
    value = np.dot(x,y) + b
    sx = 1/(1+math.e)^value
    return sx

