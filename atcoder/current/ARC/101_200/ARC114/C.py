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
        input = """2 3"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """34 56"""
        output = """649717324"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  inf = 10**18+1
  N, M = map(int, input().split(" "))

  print()

# resolve()

if __name__ == "__main__":
    unittest.main()
