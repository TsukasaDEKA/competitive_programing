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
        input = """1 2
3 4"""
        output = """-2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """0 -1
1 0"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 100
100 100"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  S = [[int(x) for x in input().split(" ")] for _ in range(2)]

  print(S[0][0]*S[1][1]-S[0][1]*S[1][0])

resolve()

if __name__ == "__main__":
    unittest.main()
