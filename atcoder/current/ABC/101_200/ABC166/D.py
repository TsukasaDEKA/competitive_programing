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
        input = """33"""
        output = """2 -1"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """1"""
        output = """0 -1"""
        self.assertIO(input, output)

def resolve():
  X= int(input())

  for A in range(-120, 120):
    for B in range(-120, 120):
      if A**5 - B**5 == X:
        print("{0} {1}".format(A, B))
        return True

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()