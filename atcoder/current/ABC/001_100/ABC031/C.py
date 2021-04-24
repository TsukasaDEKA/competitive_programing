import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """6
1 -3 3 9 1 6"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
5 5 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8
-1 10 -1 2 -1 10 -1 0"""
        output = """-1"""
        self.assertIO(input, output);

def resolve():
  inf = 10**10+1
  # N <= 50 なので全探索でいけそう。
  # 奇数番目、偶数番目で累積和取ってやると、
  # それぞれの点数が O(1) で求められるので、
  # 計算量が N*(N-1) で出せる。(ハズ)
  # インデックスがめんどい
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  odd_A = [0]*(N+1)
  even_A = [0]*(N+1)
  for i in range(N):
    if i%2:
      odd_A[i+1] = odd_A[i]
      even_A[i+1] = even_A[i]+A[i]
    else:
      odd_A[i+1] = odd_A[i]+A[i]
      even_A[i+1] = even_A[i]

  # print(A, odd_A, even_A, sep="\n")
  takahashi_score = -inf
  for t in range(1, N+1):
    aoki_score = -inf
    aoki_ans = N-1
    for a in reversed(range(1, N+1)):
      if t == a: continue
      left = min(t, a)
      right = max(t, a)
      if left % 2: tmp_aoki_score = even_A[right] - even_A[left-1]
      else: tmp_aoki_score = odd_A[right] - odd_A[left-1]

      if aoki_score <= tmp_aoki_score:
        aoki_score = tmp_aoki_score
        aoki_ans = a
    left = min(t, aoki_ans)
    right = max(t, aoki_ans)
    if left % 2: takahashi_score = max(takahashi_score, odd_A[right] - odd_A[left-1])
    else: takahashi_score = max(takahashi_score, even_A[right] - even_A[left-1])
    # print(takahashi_score, left, right)
  print(takahashi_score)
resolve()

if __name__ == "__main__":
    unittest.main()
