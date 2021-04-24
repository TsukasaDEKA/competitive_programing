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
        input = """5 7 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """11 10 9"""
        output = """9"""
        self.assertIO(input, output)

from math import floor

def resolve():
  A, B, N = map(int, input().split(" "))

  if B > N:
    print(floor(A*N/B) - A * floor(N/B))
    return
  print(floor(A*(B-1)/B))

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()