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
        input = """1000 300"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """567876543 0"""
        output = """1999432123457"""
        self.assertIO(input, output)

def resolve():
  goal = 2*(10**12)
  A, K = map(int, input().split(" "))
  if K == 0:
    print(goal-A)
  else:
    count = 0
    while A < goal:
      count+=1
      A+=1+K*A

    print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()