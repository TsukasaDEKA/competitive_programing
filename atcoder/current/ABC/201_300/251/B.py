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
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1
2 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 12
3 3 3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7 251
202 20 5 1 4 2 100"""
        output = """48"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, W = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")] + [0, 0]
  N += 2
  # print(A)

  ans = set()
  for i in range(N-2):
    for j in range(i+1, N-1):
      for k in range(j+1, N):
        n = A[i] + A[j] + A[k]
        if n > W: continue
        ans.add(n)

  print(len(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()