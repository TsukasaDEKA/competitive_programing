from os import sep
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
        input = """5 3
tokyo kanda akiba okachi ueno
tokyo akiba ueno"""
        output = """Yes
No
Yes
No
Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 7
a t c o d e r
a t c o d e r"""
        output = """Yes
Yes
Yes
Yes
Yes
Yes
Yes"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  inf = 10**18+1
  N, _ = [int(x) for x in input().split(" ")]
  S = [x for x in input().split(" ")]
  T = set([x for x in input().split(" ")])
  ans = ["No"]*N
  for i in range(N):
    if S[i] in T:
      ans[i] = "Yes"

  print(*ans, sep="\n")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()