a,b,c = map(int, input().split())

# 123
if a<b and b<c:
  print(a,b,c)
# 132
elif b>c and a<c:
  print(a,c,b)
# 213
elif a>b and a<c:
  print(b,a,c)
# 231
elif a<b and c<a:
  print(c,a,b)
# 312
elif a>c and c>b:
  print(b,c,a)
# 321
elif a>b and b>c:
  print(c,b,a)
