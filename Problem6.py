import numpy as np

#brute force calculation - because it's easy

n = 100

listOfNumbers = np.arange(n+1)

sumOfSqares = sum(np.multiply(listOfNumbers,listOfNumbers))
squareOfSums = (sum(listOfNumbers))**2

answer = squareOfSums - sumOfSqares

print answer