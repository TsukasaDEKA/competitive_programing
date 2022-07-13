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
        input = """3 2"""
        output = """2 1 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 1"""
        output = """1 2 3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 4"""
        output = """1 2 3"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """6 1"""
    #     output = """1 2 3"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """5 1"""
    #     output = """1 2 3"""
    #     self.assertIO(input, output)
def resolve():
  from bisect import bisect_left
  inf = 10**18
  # 狭義単調増加列の長さを返す。
  def lis(A):
    ans = 0
    dp = [inf]*(N-1)
    for i in range(N-1):
      index = bisect_left(dp, A[i])
      ans = max(ans, index+1)
      dp[index] = A[i]
    return ans

  N, X = map(int, input().split(" "))
  ans_0 = [X] + [( i if  i < X else  i+1) for _, i in sorted([(abs((N)-2*i),  i) for i in range(1, N)])]
  ans_1 = [X] + [(-i if -i < X else -i+1) for _, i in sorted([(abs((N)-2*i), -i) for i in range(1, N)])]

  count_0 = lis([abs(ans_0[i]-ans_0[i+1]) for i in range(N-1)])
  count_1 = lis([abs(ans_1[i]-ans_1[i+1]) for i in range(N-1)])

  print(*(ans_0 if count_0 >= count_1 else ans_1))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()