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
        input = """5 10 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 20 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 100 1"""
        output = """100"""
        self.assertIO(input, output)

def resolve():
  L, R, d = map(int, input().split(" "))

  count = 0
  for t in range(L, R + 1):
    if t%d == 0:
      count += 1
  print(count)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
