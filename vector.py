import numpy as np
from time import Timer
#It is the function to select the higher
def python_grader(a,b):
  if a >= b:
    return a
  else:
    return b
#There we apply the vectorization
numpy_grader=np.vectorize(python_grader,otypes=[int])
#There we haver aour arrays
arrX=np.array([4,5,6,14,18])
arrY=np.array([6,2,3,25,4])
#Finally, it shows our results
print(numpy_grader(arrX,arrY))
