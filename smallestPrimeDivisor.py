import numpy as np

def smallestPrimeDivisor( n ):
    primeTest = np.ones(np.ceil(pow(n,0.5)))
    primeTest[0] = 0
    
    smallestPrimeLocation = np.where(primeTest==1)
    if (np.size(smallestPrimeLocation) != 0):
        smallestPrime = smallestPrimeLocation[0][0] + 1
    
    while (n%smallestPrime != 0):
        primeTest[smallestPrime-1::smallestPrime] = 0
        smallestPrimeLocation = np.where(primeTest==1)
        if (np.size(smallestPrimeLocation) != 0):
            smallestPrime = smallestPrimeLocation[0][0] + 1
        else:
            smallestPrime = n
            break
    return smallestPrime