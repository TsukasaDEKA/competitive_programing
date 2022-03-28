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
        input = """3 7 10 3"""
        output = """24"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 5 11 3"""
        output = """20"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 8 3 3"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """3 8 2 3"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  A, B, K, L = map(int, input().split(" "))
  ans = 0
  k = K//L
  ans += k*B
  ans += min((K-k*L)*A, B)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()