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
        input = """4
taro
jiro
taro
saburo"""
        output = """taro"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
takahashikun"""
        output = """takahashikun"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9
a
b
c
c
b
c
b
d
e"""
        output = """b"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter; print(sorted(Counter([input() for _ in range(int(input()))]).items(), key=lambda x: x[1])[-1][0])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()