from smallestPrimeDivisor import smallestPrimeDivisor
import numpy as np

def allPrimeFactors( n ):

    smallestPrimeFactor = 1

    allPrimeFactors = np.array(smallestPrimeFactor)

    newQuotient = n

    while (smallestPrimeFactor != newQuotient):
        newQuotient = newQuotient/smallestPrimeFactor
        smallestPrimeFactor = smallestPrimeDivisor(newQuotient)
        allPrimeFactors = np.append(allPrimeFactors,smallestPrimeFactor)
        
    return allPrimeFactors[1:]