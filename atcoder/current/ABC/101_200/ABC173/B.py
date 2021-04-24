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
        input = """6
AC
TLE
AC
AC
WA
TLE"""
        output = """AC x 3
WA x 1
TLE x 2
RE x 0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
AC
AC
AC
AC
AC
AC
AC
AC
AC
AC"""
        output = """AC x 10
WA x 0
TLE x 0
RE x 0"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  result = {
    'AC': 0,
    'WA': 0, 
    'TLE': 0,
    'RE': 0
  }
  for i in range(N):
    result[input()] += 1
  print('AC x', result['AC'])
  print('WA x', result['WA'])
  print('TLE x', result['TLE'])
  print('RE x', result['RE'])

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
