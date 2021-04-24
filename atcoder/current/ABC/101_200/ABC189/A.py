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
        input = """SSS"""
        output = """Won"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """WVW"""
        output = """Lost"""
        self.assertIO(input, output)

def resolve():
  S = list(input())

  print("Won" if S[0] == S[1] and S[0] == S[2] else "Lost")

resolve()

if __name__ == "__main__":
    unittest.main()
