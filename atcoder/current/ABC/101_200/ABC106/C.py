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
        input = """1214
4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
157"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """299792458
9460730472580800"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A = [int(x) for x in list(input())]+[2]
  N = len(A)
  K = int(input())
  i = 0
  while A[i] == 1:
    i+=1
  ans = A[:i+1]

  print(ans[min(K, len(ans))-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()