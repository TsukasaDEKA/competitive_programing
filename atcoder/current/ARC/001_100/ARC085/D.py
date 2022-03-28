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
        input = """3 100 100
10 1000 100"""
        output = """900"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 100 1000
10 100 100"""
        output = """900"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 1 1
1 1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 1 1
1000000000"""
        output = """999999999"""
        self.assertIO(input, output)

def resolve():
  # 複雑なことをやりそうだけど、実の所最後の 2 枚しか関係なさそう。
  N, Z, W = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  if N == 1:
    print(abs(A[0]-W))
    return
  A = A[-2:]
  print(max(abs(A[0]-A[1]), abs(A[1]-W)))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()