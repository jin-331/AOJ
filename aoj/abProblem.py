import decimal
a, b = map(float, input().split())
d = a//b
r = a%b
f = a/b
print(int(d), int(r), '{:.10f}'.format(f))