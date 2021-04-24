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
        input = """Y
a"""
        output = """A"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """N
b"""
        output = """b"""
        self.assertIO(input, output)

def resolve():
  S = input()
  T = input()

  print(T.upper() if S=="Y" else T)

if __name__ == "__main__":
  resolve()


if __name__ == "__main__":
    unittest.main()
