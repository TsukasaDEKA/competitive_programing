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
        input = """3
acornistnt
peanutbomb
constraint"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
oneplustwo
ninemodsix"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
  from collections import defaultdict
  N = int(input())
  agg = defaultdict(int)
  for _ in range(N):
    S = "".join(sorted(list(input())))
    agg[S]+=1

  ans = 0
  for v in agg.values():
    ans += (v*(v-1))//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()