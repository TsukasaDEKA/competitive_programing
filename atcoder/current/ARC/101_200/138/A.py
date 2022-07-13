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
        input = """4 2
2 1 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 1
3 2 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20 13
90699850 344821203 373822335 437633059 534203117 523743511 568996900 694866636 683864672 836230375 751240939 942020833 865334948 142779837 22252499 197049878 303376519 366683358 545670804 580980054"""
        output = """13"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  A = sorted([(a, -i) for i, a in enumerate(A)])

  ans = inf
  max_i = -inf
  for n in range(N):
    _, i = A[n]
    i *= -1
    if i >= K:
      ans = min(ans, i - max_i)
    else:
      max_i = max(max_i, i)


  print(ans if ans < inf else -1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()