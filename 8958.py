n = int(input())
for i in range(n):
    l = input()
    B = list(l)
    sum = 0
    c = 1
    for i in B:
        if i == "O":
            sum += c
        c += 1
        if i == "X":
            c = 1
    print(sum)