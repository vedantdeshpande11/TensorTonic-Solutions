import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x1 = np.array(x)
    y1 = np.array(y)
    return np.sqrt(np.sum((x1-y1)**2))