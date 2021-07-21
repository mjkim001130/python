a = int(input())
b = int(input())
c = int(input())

num = a*b*c

cnt = []
for i in str(num):
    cnt.append(i)

cnt = list(map(int, cnt))
print(cnt.count(0))
print(cnt.count(1))
print(cnt.count(2))
print(cnt.count(3))
print(cnt.count(4))
print(cnt.count(5))
print(cnt.count(6))
print(cnt.count(7))
print(cnt.count(8))
print(cnt.count(9))