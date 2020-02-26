
for i in range(0,10000):
  a, op, b = input().split()
  a = int(a)
  b = int(b)
  if op == "?":
    break
  elif op == "+":
    print(a+b)
  elif op == "-":
    print(a-b)
  elif op == "*":
    print(a*b)
  elif op == "/":
    print(a//b)