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
        input = """5
10 3 5 2 3 6
10 3 5 1 1000000000 1000000000
139 2 139 1 1 1
139 1 1 1 1 1
139 7 10 3845 26982 30923"""
        output = """11
10
1
139
436604"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())
  for _ in range(T):
    # 1 を使いたくないパターンがあるっぽい。
    # 1 のコストがとても高いとか。
    N,A,B,X,Y,Z = map(int, input().split(" "))
    P = 0

    # コスパが悪いならば A, B は使わない。
    if A*X <= Y: A, Y = 1, X
    if B*X <= Z: B, Z = 1, X
    if Z == X and B == 1 and Y == X and A == 1:
      print(N*X)
      continue
    if Z == X and B == 1:
      print((N//A)*Y + (N%A)*X)
      continue
    if Y == X and A == 1:
      print((N//B)*Z + (N%B)*X)
      continue
    print(N,A,B,X,Y,Z)
    # できるだけ 1 を使わない方針で考えよう
    # 1 


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()