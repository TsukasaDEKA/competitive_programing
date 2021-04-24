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
        input = """0 10
0 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """-100 -100
100 100"""
        output = """-200"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """-100 100
-100 100"""
        output = """200"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1

  A, B = map(int, input().split(" "))
  C, D = map(int, input().split(" "))

  print(B-C)

resolve()

if __name__ == "__main__":
    unittest.main()
