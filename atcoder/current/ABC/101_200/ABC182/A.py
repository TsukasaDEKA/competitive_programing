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
        input = """200 300"""
        output = """200"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10000 0"""
        output = """20100"""
        self.assertIO(input, output)

def resolve():
  A, B = map(int, input().split(" "))

  max_follow = 2*A+100

  print(max_follow-B)

resolve()

if __name__ == "__main__":
    unittest.main()
