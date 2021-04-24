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
        input = """2
1
1"""
        output = """0
1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
1
4
1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3
1
2
3"""
        output = """0
1
3"""
        self.assertIO(input, output)

def resolve():
  # A_0 を 0 にすると A_1 = B_0, A_N = B_N になる。
  # また、A_i^A_i-1 = B_i-1 なので、
  # A_i^A_i-1^A_i-1 = A_i = A_i-1^B_i-1
  L = int(input())
  B = [int(input()) for _ in range(L)]
  A = [0]*L
  for i in range(1, L):
    A[i] = A[i-1]^B[i-1]

  if A[-1] != B[-1]:
    print(-1)
    return
  print(*A, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
