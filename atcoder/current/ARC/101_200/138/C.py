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
        input = """4
3 4 1 2"""
        output = """1 7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 1"""
        output = """0 1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
716893678 779607519 555600775 393111963 950925400 636571379 912411962 44228139 15366410 2063694"""
        output = """7 3996409938"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
1 2 3 4 5 6"""
        output = """0 15"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  sortedA = sorted([(x, i) for i, x in enumerate(A)], reverse=True)

  total = 0
  target_i = []
  for i in range(N//2):
    x, j = sortedA[i]
    total+=x
    target_i.append(j)
  
  target_i.sort()
  target_i.append(N+target_i[0])
  diff = 0
  k = 0
  for i in range(len(target_i)-1):
    if target_i[i+1] - target_i[i] > diff:
      diff = target_i[i+1] - target_i[i]
      k = target_i[i]

  print((k+1)%N, total)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()

