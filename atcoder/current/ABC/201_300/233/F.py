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
        input = """6
5 3 2 4 6 1
4
1 5
5 6
1 2
2 3"""
        output = """3
4 2 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 4 1 2 5
2
1 3
2 5"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1 2 3 4
6
1 2
1 3
1 4
2 3
2 4
3 4"""
        output = """0

4
5 5 5 5"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  N, K = map(int, input().split(" "))
  A = [[int(x)+i, i-int(x)] for i, x in enumerate(input().split(" "))]
  A = [int(x) for x in input().split(" ")]
  A = [int(input()) for _ in range(N)]
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  S = list(input())
  S_map = [list(input()) for _ in range(H)]

  print()


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()