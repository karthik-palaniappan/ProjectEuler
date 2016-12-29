import numpy as np
import matplotlib

# not the perfect algorithm - finds primes upto some arbitrary large number and
# stops when the nth prime is reached.

def findPrimeN ( n ):
    sieveOFEratosthenes = np.ones(1000000) # currently upto 10 Million
    sieveOFEratosthenes[0] = 0
    sieveOFEratosthenes[1] = 0
    
    sieveOFEratosthenes[2] = 0
    listOfPrimes = np.array([2])
    currPrime = 2
    sieveOFEratosthenes[currPrime::currPrime] = 0
    primeCount = 1
    
    while (primeCount < n):
        currPrime = np.where(sieveOFEratosthenes==1)[0][0]
        sieveOFEratosthenes[currPrime::currPrime] = 0
        listOfPrimes = np.append(listOfPrimes,currPrime)
        primeCount = primeCount + 1
    
    return listOfPrimes[-1]