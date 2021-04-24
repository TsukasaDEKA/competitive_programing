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
        input = """apple"""
        output = """
        """
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """bus"""
        output = """buses"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """box"""
        output = """boxs"""
        self.assertIO(input, output)

def resolve():
  S = input()

  print(S+"s" if S[-1] != "s" else S+"es")

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
