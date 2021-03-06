import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """2 3 1"""
        output = """1.0000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 180707 0"""
        output = """0.0001807060"""
        self.assertIO(input, output)

def resolve():
  # 解説 AC
  # 
  N, M, D = map(int, input().split(" "))
  ans = M-1
  ans *= 2*(N-D)/(N**2) if D != 0 else 1/N

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
