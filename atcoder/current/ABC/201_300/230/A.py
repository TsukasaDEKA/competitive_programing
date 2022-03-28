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
        input = """42"""
        output = """AGC043"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """19"""
        output = """AGC019"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1"""
        output = """AGC001"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """50"""
        output = """AGC051"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  if N < 42:
    print("AGC"+str(N).zfill(3))
  else:
    print("AGC"+str(N+1).zfill(3))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()