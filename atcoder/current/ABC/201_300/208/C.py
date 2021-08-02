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
        input = """2 7
1 8"""
        output = """4
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 3
33"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7 1000000000000
99 8 2 4 43 5 3"""
        output = """142857142857
142857142857
142857142858
142857142857
142857142857
142857142857
142857142857"""
        self.assertIO(input, output)


def resolve():
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  sorted_A = sorted([(x, i) for i, x in enumerate(A)])

  count = K//N
  K%=N
  ans = [count]*N
  for i in range(K):
    x, j = sorted_A[i]
    ans[j] += 1
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()