n = int(input())
score = list(map(int, input().split()))
m_score = max(score)
avg = 0
for i in range(len(score)):
    score[i] = (score[i] / m_score) * 100
    avg += score[i] / len(score)
print(avg)