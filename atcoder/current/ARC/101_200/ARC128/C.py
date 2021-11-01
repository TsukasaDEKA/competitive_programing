import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3 2 3
1 2 3"""
        output = """8.00000000000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 2
5 1 1"""
        output = """4.66666666666666666667"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 234567 1000000
353239 53676 45485 617014 886590 423581 172670 928532 312338 981241"""
        output = """676780145098.25000000000000000000"""
        self.assertIO(input, output)

def resolve():
  # 後ろから見ていって、最大の物に可能な限りぶっこむのが最適。
  # A を 1 ~ N で割った値を考える。区間長 +1
  # <その時点で与えられる最大の x>/(r-l) * (sum(A[l:r])) が最大になるようにすれば良いので、
  # (sum(A[l:r]))/(r-l) が増え続ける限り l を伸ばしていって・・・と言うのを繰り返せば良さそう。
  inf = 10**18+1
  N, M, S = map(int, input().split(" "))
  A = list(reversed([int(x) for x in input().split(" ")]))
  # 平均値が最大の区間を求めて、愚直にやっていく。
  sum_A = [0]*(N+1)
  for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]
  
  # print(sum_A)
  val = S
  ans = 0
  l = 0
  while l < N:
    temp_avr = 0
    r = l+1
    for r_ in range(l+1, N+1):
      if temp_avr <= (sum_A[r_]-sum_A[l])/(r_-l):
        temp_avr = (sum_A[r_]-sum_A[l])/(r_-l)
        r = r_
    v = min(M, val/(r-l))
    ans+=v*temp_avr*(r-l)
    # print(v*temp_avr, temp_avr, v)
    val-=v*(r-l)
    l = r

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()