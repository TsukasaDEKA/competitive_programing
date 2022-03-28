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
        input = """2 4
0 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 4
0 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 1000000000
0 1000 1000000 1000000000"""
        output = """2000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 1
0"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """9 10
0 3 5 7 100 110 200 300 311"""
        output = """67"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, T = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]+[inf]
  ans = 0
  for i in range(N):
    ans+=min(T, A[i+1]-A[i])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()