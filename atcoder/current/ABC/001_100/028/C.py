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
        input = """1 2 3 4 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 2 3 5 8"""
        output = """14"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A = [int(x) for x in input().split(" ")]
  ans = set()
  for i in range(3):
    for j in range(i+1, 4):
      for k in range(j+1, 5):
        ans.add(A[i]+A[j]+A[k])

  ans = sorted(list(ans), reverse=True)[2]
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()