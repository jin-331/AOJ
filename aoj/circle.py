w, h, x, y, r = map(int, input().split())

if x<=0 or y<=0:
  print('No')
elif x+r <= w and y+r <= h:
  print('Yes')
else:
  print('No')

