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
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  S = [[int(x)-1 for x in input().split(" ")][1:] for _ in range(M)]
  P = [int(x) for x in input().split(" ")]

  ans = 0
  for b in range(1<<N):
    for i in range(M):
      count = 0
      for s in S[i]:
        if b&(1<<s):
          count += 1
      if count%2 != P[i]:
        break
    else:
      ans += 1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()