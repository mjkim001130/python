a = []
b = 42
for i in range(10):
    a.append(input())
a = list(map(int, a))
div = [a[i] % 42 for i in range(len(a))]
div = set(div)
print(len(div))
