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
        input = """333"""
        output = """65287.907678222"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """634"""
        output = """90086.635834623"""
        self.assertIO(input, output)

def resolve():
  from math import sqrt
  H = int(input())

  print(sqrt(H*(12800000+H)))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()