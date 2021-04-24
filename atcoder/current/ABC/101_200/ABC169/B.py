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
        input = """2
1000000000 1000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
101 9901 999999000001"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31
4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0"""
        output = """0"""
        self.assertIO(input, output)



def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  maximam = 10**18

  result = 1
  if 0 in A:
    print(0)
    return True

  for a in A:
    result *= a
    if result > maximam:
      print(-1)
      return True
  print(result)

# if __name__ == "__main__":
#     resolve()

if __name__ == "__main__":
    unittest.main()
