a,b = input().split()
reversed_a = a[::-1]
reversed_b = b[::-1]
if int(reversed_a) > int(reversed_b):
    print(int(reversed_a))
else:
    print(int(reversed_b))