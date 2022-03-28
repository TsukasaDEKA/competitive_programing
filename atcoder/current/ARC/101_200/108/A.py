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
        input = """3 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000000 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20 100"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  S, P = map(int, input().split(" "))
  maximam = 10**6
  for i in range(1, maximam+1):
    if P == S*i-i**2:
      print("Yes")
      return
  print("No")

resolve()

if __name__ == "__main__":
    unittest.main()
