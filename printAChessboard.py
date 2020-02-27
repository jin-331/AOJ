while True:
  H, W = map(int, input().split())
  if H==0 and W==0:
    break
  for i in range(H):
    if i == 0 or i%2 == 0:
      for j in range(W):
        if j == 0 or j%2 == 0:
          print("#",end="")
        else:
          print(".",end="")
      print()#改行
    else:
      for j in range(W):
        if j == 0 or j%2 == 0:
          print(".",end="")
        else:
          print("#",end="")
      print()#改行
  print()
    