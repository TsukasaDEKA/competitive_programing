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
        input = """100 1 2"""
        output = """101"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100 2 1"""
        output = """99"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 1 1"""
        output = """100"""
        self.assertIO(input, output)

def resolve():
  N, A, B = map(int, input().split(" "))

  print(N-A+B)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    import sys

    print(sys.version)

    unittest.main()
