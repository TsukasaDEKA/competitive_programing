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
        input = """3 1
178 205 132
112 220 96
36 64 20"""
        output = """Yes
Yes
No"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1
300 300 300
200 200 200"""
        output = """Yes
Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 2
127 235 78
192 134 298
28 56 42
96 120 250"""
        output = """Yes
Yes
No
Yes"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect

  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = [sum([int(x) for x in input().split(" ")]) for _ in range(N)]
  table = sorted(A)
  # A = sorted([(x, i) for i, x in enumerate([sum([int(x) for x in input().split(" ")]) for _ in range(N)])], reverse=True)
  ans = [""]*N
  for i in range(N):
    index = bisect(table, A[i]+300)
    ans[i] = "Yes" if N-index+1 <= K else "No"
  print(*ans, sep="\n")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()