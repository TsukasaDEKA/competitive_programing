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
        input = """2 10
3 6
4 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 10
10 100
10 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 12
1 8
5 7
3 4
2 6"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, X = [int(x) for x in input().split(" ")]
  pos = set()
  pos.add(0)
  for _ in range(N):
    A, B = [int(x) for x in input().split(" ")]
    temp = set()
    for i in pos:
      if i+A <= X: temp.add(i+A)
      if i+B <= X: temp.add(i+B)
    pos = temp
  print("Yes" if X in pos else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()