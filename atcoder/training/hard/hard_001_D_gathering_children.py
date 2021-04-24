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
        input = """RRLRL"""
        output = """0 1 2 1 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """RRLLLLRLRRLL"""
        output = """0 3 3 0 0 0 1 1 0 2 2 0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """RRRLLRLLRRRLLLLL"""
        output = """0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0"""
        self.assertIO(input, output)

from math import ceil, floor

def resolve():
  S = list(input())
  N = len(S)
  result = ["0"]*N

  # print("S:", S, ", N:", N)

  start_index = 0
  while True:
    R_index = start_index
    R_length = 1
    while S[R_index+1] == "R":
      R_length += 1
      R_index += 1

    L_index = R_index+1
    end_index = L_index
    L_length = 1
    if end_index+1 <= N-1:
      while S[end_index+1] == "L":
        L_length += 1
        if end_index+1 >= N-1:
          break
        else:
          end_index += 1

    result[R_index] = str(ceil(R_length/2) + L_length//2)
    result[L_index] = str(ceil(L_length/2) + R_length//2)

    if end_index + 1 >= N - 1:
      break

    start_index = end_index + 1
  print(" ".join(result))

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
