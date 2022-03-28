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
1 2
6 6
4 4
3 3
3 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 1
2 2
3 4
5 5
6 6"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
1 1
2 2
3 3
4 4
5 5
6 6"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  for i in range(N-2):
    for j in range(i, i+3):
      d1, d2 = A[j]
      if d1 != d2: break
    else:
      print("Yes")
      return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()