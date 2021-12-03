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
        input = """4"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100"""
        output = """323"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100000000000"""
        output = """5745290566750"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())

  ans = 0
  for a in range(1, int(-(-N**0.5//1))+1):
    B = N//a
    for b in range(a, int(-(-B**0.5//1))+1):
      C = N//(a*b)
      ans += max(0, C-b+1)
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()