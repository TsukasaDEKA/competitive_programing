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
        input = """7 3
3 2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 3
1 4 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 1
100"""
        output = """99"""
        self.assertIO(input, output)

def resolve():
  K, T = map(int, input().split(" "))
  print(max(0, 2*max([int(x) for x in input().split(" ")])-K-1))
# resolve()

if __name__ == "__main__":
    unittest.main()
