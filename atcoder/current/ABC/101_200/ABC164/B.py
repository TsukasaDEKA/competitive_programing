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
        input = """10 9 10 10"""
        output = """No"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """46 4 40 5"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  A, B, C, D = map(int, input().split(" "))

  winner = True
  while True:
    C -= B
    if (C <= 0):
      winner = True
      break

    A -= D
    if (A <= 0):
      winner = False
      break

  print("Yes" if winner else "No")

# if __name__ == "__main__":
#     resolve()

if __name__ == "__main__":
    unittest.main()