import itertools
import time

w = []
p = []
f = open("C:/Users/DELL/Desktop/studia/2-semestr/algorytmy-i-struktury-danych/problem-plecakowy/dane.txt", "r")
c = int(f.readline())
n = int(f.readline())
for i in range(n):
    a = f.readline()
    x, y = a.split()
    p.append(int(x))
    w.append(int(y))


def Bellman(c, w, p):
    m = []
    n = len(w)
    for i in range(n+1):
        m.append([0]*(c+1))
    for i in range(1, n+1):
        for j in range(1, c+1):
            if w[i-1] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = max(m[i-1][j], m[i-1][j-w[i-1]]+p[i-1])
    maksimum = m[n][c]
    solution = []
    i = n
    j = c
    while i > 0:
        if m[i-1][j] != m[i][j]:
            solution.append(i)
            j = j-w[i-1]
        i = i-1
    return maksimum, solution, m


def brute_force(c, w, p):
    maksimum = 0
    n = len(w)
    l = [x for x in itertools.product([1, 0], repeat=n)]
    for x in l:
        wynik = 0
        masa = 0
        for i in range(n):
            wynik += p[i]*x[i]
            masa += w[i]*x[i]
        if masa <= c:
            if wynik > maksimum:
                maksimum = wynik
                solution = x
        result = []
    for i in range(n):
        if solution[i] == 1:
            result.append(i+1)
    return maksimum, result


start = time.time()
a, b, mm = Bellman(c, w, p)
stop = time.time()
print(stop-start)
print(a)
print(b)
# for i in mm:
#     print(i)

start = time.time()
c, d = brute_force(c, w, p)
stop = time.time()
print(stop-start)
print(c)
print(d)
