import random
import time

N = 10**5  # 配列のサイズ
M = 10**4  # 探索の繰り返し回数
a = 2021   # 配列の中から探索する数値

A = [random.randint(1, N) for i in range(N)]
A.sort()


# 線形探索(O(N))
def linear_search1(A, a):
    return a in A


# 二部探索(O(log(N)))
def binary_search2(A, a):
    l = 0
    r = len(A)
    while r-l > 1:
        m = (r+l)//2
        if A[m] > a:
            r = m
        elif A[m] < a:
            l = m
        elif A[m] == a:
            return True
    return False


# 関数fの実行時間計測関数
def measure_time(f, A, a):
    start = time.time()
    print(f(A, a))
    for i in range(M):
        f(A, a)
    print(time.time()-start)


# それぞれの関数の実行時間を計測
measure_time(linear_search1, A, a)
measure_time(binary_search2, A, a)
