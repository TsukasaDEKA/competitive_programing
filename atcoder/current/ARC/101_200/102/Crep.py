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
        input = """3 2"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31415 9265"""
        output = """27"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """35897 932"""
        output = """114191"""
        self.assertIO(input, output)

def resolve():
  N, K = map(int, input().split(" "))
  ans = pow(N//K, 3)
  if K%2 == 0:
    p = (N-K//2)//K+1
    ans += pow(max(0, p), 3)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()