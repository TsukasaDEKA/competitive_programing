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
        input = """2 1 1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2000000000 0 0 2000000000"""
        output = """2000000000"""
        self.assertIO(input, output)

def resolve():
  A, B, C, K = map(int, input().split(" "))
  ans = min(K, A)
  K -= min(K, A)
  K -= min(K, B)
  ans -= min(K, C)
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()