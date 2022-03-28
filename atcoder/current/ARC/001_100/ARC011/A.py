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
        input = """2 1 8"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 4 30"""
        output = """62"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 99 1000"""
        output = """90199"""
        self.assertIO(input, output)



def resolve():
  M, N, T = [int(x) for x in input().split(" ")]
  ans = T
  while T >= M:
    ans += (T//M)*N
    T = (T//M)*N + T%M
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()