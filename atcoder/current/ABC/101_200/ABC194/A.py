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
        input = """10 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0 0"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A, B = map(int, input().split(" "))

  base = A+B
  if base >= 15 and B >= 8:
    print(1)
    return
  if base >= 10 and B >= 3:
    print(2)
    return
  if base >= 3:
    print(3)
    return
  print(4)

resolve()

if __name__ == "__main__":
    unittest.main()
