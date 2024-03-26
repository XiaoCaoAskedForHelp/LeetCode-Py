with open('./records.txt', 'r', encoding="utf-8") as f:
    times = f.readlines()
times.sort()


def counts(h, m, s):
    return s + m * 60 + h * 60 * 60


cnt = 0
for i in range(0, len(times), 2):
    h1, m1, s1 = map(int, times[i].split(' ')[1].split(':'))
    h2, m2, s2 = map(int, times[i + 1].split(' ')[1].split(':'))
    counts1 = counts(h1, m1, s1)
    counts2 = counts(h2, m2, s2)
    cnt += (counts2 - counts1)
print(cnt)
