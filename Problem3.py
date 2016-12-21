from smallestPrimeDivisor import smallestPrimeDivisor
import numpy as np

n = 600851475143

smallestPrimeFactor = 1

allPrimeFactors = np.array(smallestPrimeFactor)

newQuotient = n

while (smallestPrimeFactor != newQuotient):
    newQuotient = newQuotient/smallestPrimeFactor
    smallestPrimeFactor = smallestPrimeDivisor(newQuotient)
    allPrimeFactors = np.append(allPrimeFactors,smallestPrimeFactor)


print allPrimeFactors[-1]