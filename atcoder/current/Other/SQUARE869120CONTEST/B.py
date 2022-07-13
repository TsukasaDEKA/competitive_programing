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
5 7
2 6
8 10"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 71
43 64
13 35
14 54
79 85"""
        output = """334"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11
15004200 341668840
277786703 825590503
85505967 410375631
797368845 930277710
90107929 763195990
104844373 888031128
338351523 715240891
458782074 493862093
189601059 534714600
299073643 971113974
98291394 443377420"""
        output = """8494550716"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  target = set()
  for a, b in A:
    target.add(a)
    target.add(b)

  target = sorted(list(target))
  ans = inf
  for i in range(len(target)):
    s = target[i]
    for j in range(i, len(target)):
      g = target[j]
      temp = 0
      for i in range(N):
        a, b = A[i]
        # print(abs(a-s), (b-a-1), abs(b-g))
        temp += abs(a-s) + (b-a) + abs(b-g)
      # print(s, g, temp)
      ans = min(ans, temp)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()