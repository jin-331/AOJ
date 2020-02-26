n = int(input())
a = list(map(int, input().split()))
print(min(a), max(a), sum(a))
  
BIG_NUM  = 2000000000
maximum  = -BIG_NUM
minimum = BIG_NUM
total = 0

for x in a:
  if maximum < x:
    maximum = x
  if minimum > x:
    minimum = x
  total += x

print("%d %d %d"%(minimum, maximum, total))
