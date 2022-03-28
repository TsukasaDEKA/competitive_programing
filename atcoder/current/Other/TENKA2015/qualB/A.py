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
        input = """41 2
5 6"""
        output = """30"""
        self.assertIO(input, output)

def resolve():
  N = 20
  ans = [0]*N
  ans[0] = 100
  ans[1] = 100
  ans[2] = 200
  for i in range(3, N):
    # print(ans[i-3:i])
    ans[i] = sum(ans[i-3:i])
  print(ans[-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()