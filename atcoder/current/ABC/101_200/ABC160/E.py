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
        input = """1 2 2 2 1
2 4
5 1
3"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2 2 2 2
8 6
9 1
2 1"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 2 4 4 4
11 12 13 14
21 22 23 24
1 2 3 4"""
        output = """74"""
        self.assertIO(input, output)

def resolve():
  # 解説
  X, Y, A, B, C = map(int, input().split(" "))
  RED = sorted([int(x) for x in input().split(" ")])[A-X:]
  GREEN = sorted([int(x) for x in input().split(" ")])[B-Y:]
  WHITE = sorted([int(x) for x in input().split(" ")], reverse=True)

  APPLES = RED+GREEN+WHITE
  APPLES.sort(reverse=True)

  print(sum(APPLES[:X+Y]))
resolve()


if __name__ == "__main__":
    unittest.main()
