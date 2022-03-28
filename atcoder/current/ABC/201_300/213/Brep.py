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
1 123 12345 12 1234 123456"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 1 4 15 9"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = sorted([(i, int(x)) for i, x in enumerate(input().split(" "))], key=lambda x: x[1])

  print(A[-2][0]+1)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()