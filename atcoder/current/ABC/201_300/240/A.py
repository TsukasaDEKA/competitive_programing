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
        input = """4 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 5"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 10"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  a, b = map(int, input().split(" "))
  if a+1 == b or (a == 1 and b == 10):
    print("Yes")
  else:
    print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()