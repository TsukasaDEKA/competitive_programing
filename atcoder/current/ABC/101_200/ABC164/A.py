import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
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
        output = """unsafe"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """100 2"""
        output = """safe"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """10 10"""
        output = """unsafe"""
        self.assertIO(input, output)

def resolve():
  S, W = map(int, input().split(" "))
  print('unsafe' if S <= W else "safe")

if __name__ == "__main__":
    unittest.main()