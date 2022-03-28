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
        input = """4 3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3141592 6535897 9323846"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2 4 1"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  A, B, C = map(int, input().split(" "))
  print(pow(A%10, pow(B, C, 4)+4, 10))
resolve()

if __name__ == "__main__":
    unittest.main()
