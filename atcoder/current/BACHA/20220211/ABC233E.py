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
        input = """1225"""
        output = """1360"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """99999"""
        output = """111105"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314159265358979323846264338327950288419716939937510"""
        output = """349065850398865915384738153697722542688574377708317"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ

  # 500000桁の整数。
  # 一度末尾から累積和
  X = [int(x) for x in list(input())]
  N = len(X)
  sumX = list(accumulate(X))[::-1]
  offset = 8
  ans = [0]*(N+offset)
  for i in range(N):
    listX = [int(x) for x in list(str(sumX[i]))][::-1]
    lenX = len(listX)
    for n in range(lenX):
      ans[i+n] += listX[n]
      if ans[i+n] >= 10:
        ans[i+n+1] += ans[i+n]//10
        ans[i+n] %= 10
  ans = ans[::-1]
  i = 0
  while ans[i] == 0:
    i+=1
  ans = ans[i:]
  print(*ans, sep="")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()