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
        input = """47"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """-24"""
        output = """-3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """50"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """-30"""
        output = """-3"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """987654321987654321"""
        output = """98765432198765432"""
        self.assertIO(input, output)

def resolve():
  X = int(input())
  print(X//10)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()