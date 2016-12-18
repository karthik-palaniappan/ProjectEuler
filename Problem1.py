from findMultiplesOf import findMultiplesOf

nBegin = 0
nEnd = 1000

s3 = sum(findMultiplesOf(nBegin,nEnd,3))
s5 = sum(findMultiplesOf(nBegin,nEnd,5))
s15 = sum(findMultiplesOf(nBegin,nEnd,15))

answer = s3+s5-s15 #multiples of both 3 and 5 (ie multiples of 15) are counted twice, and so their sum needs to be subtracted

print answer