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
        input = """106"""
        output = """4 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1024"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10460353208"""
        output = """21 1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6"""
        output = """0 1"""
        self.assertIO(input, output)


    # def test_Sample_Input_3(self):
    #     input = """1046035300"""
    #     output = """21 1"""
    #     self.assertIO(input, output)

def resolve():
  N = int(input())
  multipul_three = 3
  multipul_five = 5
  A = 1
  B = 1

  while multipul_three < N:
    dist = N - multipul_three
    while dist - multipul_five > 0:
      multipul_five *= 5
      B += 1
    
    if dist - multipul_five == 0:
      print(A, B)
      return True
    else:
      multipul_five = 5
      B = 1

    multipul_three *= 3
    A += 1
  # print(A, B)

  print(-1)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
