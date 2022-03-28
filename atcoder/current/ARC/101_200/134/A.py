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
        input = """2 10 3
3 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 10 3
0 1 4 6 7"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """12 1000000000 5
18501490 45193578 51176297 126259763 132941437 180230259 401450156 585843095 614520250 622477699 657221699 896711402"""
        output = """199999992"""
        self.assertIO(input, output)

def resolve():
  N, L, W = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]+[L]

  ans = 0
  current = 0
  for i in range(N+1):
    if A[i] > current:
      temp = ((A[i]-current)+W-1)//W
      ans += temp
    current = A[i]+W

  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()