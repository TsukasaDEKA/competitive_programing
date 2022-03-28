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
        input = """4 2 6"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 3 4"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314159265 35897932 384626433"""
        output = """48518828981938099"""
        self.assertIO(input, output)

def resolve():
  K, A, B = map(int, input().split(" "))
  if A+2 >= B:
    print(1+K)
    return

  K-=(A-1)
  ans = A
  ans += (K//2)*(B-A)
  ans += K%2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()