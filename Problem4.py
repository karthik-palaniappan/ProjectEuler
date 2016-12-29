import numpy as np

numIndex = np.arange(9,-1,-1)
truthIndex = False


for a in np.arange(9,0,-1):
    for b in numIndex:
        for c in numIndex:
            for m in np.arange(990,0,-11):
                palindrome = 11*(9091*a+910*b+100*c)
                n = palindrome/m
                if ( (palindrome%m == 0) & (n/1000 == 0)):
                    truthIndex = True
                if (truthIndex):
                    break
            if (truthIndex):
                break
        if (truthIndex):
            break
    if (truthIndex):
        break
print palindrome, m, palindrome/m, a, b, c