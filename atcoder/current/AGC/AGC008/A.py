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
        input = """10 20"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 -10"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """-10 -20"""
        output = """12"""
        self.assertIO(input, output)

def resolve():
  x, y = map(int, input().split(" "))
  abs_x, abs_y = abs(x), abs(y)
  count = 0
  if abs_x < abs_y and x < 0:
    count+=1
    x *= -1
  if abs_x > abs_y and x >= 0:
    count+=1
    x *= -1

  count+=abs(abs_y-abs_x)
  x+=abs(abs_y-abs_x)

  if x*y < 0: count+=1
  print(count)

resolve()

if __name__ == "__main__":
    unittest.main()
