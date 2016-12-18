import numpy as np

def listFibonacci( nEnd ):
        
    fibArray = np.array([0,1])
    
    newFib = fibArray[-1] + fibArray[-2]
    
    while (newFib < nEnd):
        fibArray = np.append(fibArray,newFib)
        newFib = fibArray[-1] + fibArray[-2]
    
    return fibArray