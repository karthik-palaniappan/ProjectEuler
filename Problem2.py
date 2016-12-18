from fibonacci import listFibonacci

nEnd = 4000000

lFib = listFibonacci(nEnd)

answer = sum(lFib[0::3])

print answer