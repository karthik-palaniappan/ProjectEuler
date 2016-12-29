import numpy as np
from allPrimeFactors import allPrimeFactors

def lcm ( listOfNumbers ):
    biggestNumber = max(listOfNumbers)
    primePowers = np.zeros(biggestNumber+1)
    for i in listOfNumbers:
        currPrimeFactors = np.bincount(allPrimeFactors(i))
        currPrimeFactors = np.append(currPrimeFactors,np.zeros(biggestNumber+1-len(currPrimeFactors)))
        primePowers = np.maximum(primePowers, currPrimeFactors)
    numbers = np.arange(biggestNumber+1)
    lcm = np.prod(np.power(numbers, primePowers)[2:])
    return lcm