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
        input = """3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100"""
        output = """473"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000"""
        output = """13969985"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  count = 0

  for A in range(1, N):
    count += ((N-1)//A)
  print(count)

  # for c in range(1, N-1):
  #   factorized = factorization(N-c)
  #   num_of_pattern = 1
  #   even_flag = True
    
  #   for segment in factorized:
  #     num_of_pattern *= segment[1] + 1

  #     if segment[1] % 2 == 1:
  #       even_flag = False

  #   count += num_of_pattern

  # print(count)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
