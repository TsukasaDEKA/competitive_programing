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
        input = """1
1024"""
        output = """1024
1024"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
3
4
5"""
        output = """12
0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
512
512"""
        output = """1024
0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3
4
8
1"""
        output = """13
3"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """10
1
2
3
4
5
6
7
8
9
10"""
        output = """55
0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  D = [int(input()) for _ in range(N)]
  # 最大値は簡単
  print(sum(D))

  if N == 1:
    print(sum(D))
  elif N == 2:
    print(abs(D[0]-D[1]))
  else:
    print(max(0, 2*max(D) - sum(D)))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()