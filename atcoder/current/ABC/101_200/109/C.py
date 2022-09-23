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
        input = """3 3
1 7 11"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 81
33 105 57"""
        output = """24"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1
1000000000"""
        output = """999999999"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  # 最大公約数
  N, X = map(int, input().split(" "))
  X = [abs(int(x)-X) for x in input().split(" ")]
  ans = max(X)
  for i in range(N):
    if X[i] == 0: continue
    ans = gcd(ans, X[i])

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()