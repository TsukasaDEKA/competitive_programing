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
        input = """3 5
3 1
4 2
2 3"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 100
6 2
1 5
3 9
8 7"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 3141
314944731 649
140276783 228
578012421 809
878510647 519
925326537 943
337666726 611
879137070 306
87808915 39
756059990 244
228622672 291"""
        output = """2357689932073"""
        self.assertIO(input, output)

def resolve():
  # 美味しいチーズを可能な限り多く使いたい。
  N, W = map(int, input().split(" "))
  CHEESE = sorted([[int(x) for x in input().split(" ")] for _ in range(N)], reverse=True)
  ans = 0
  for i in range(N):
    a, b = CHEESE[i]
    ans += a*min(b, W)
    W-=min(b, W)
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()