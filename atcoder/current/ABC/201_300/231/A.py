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
        input = """1000"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """50"""
        output = """0.5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3141"""
        output = """31.41"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  D = int(input())


  print(D/100)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()