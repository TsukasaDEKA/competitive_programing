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

    def test_入力例_1(self):
        input = """3 7 3
1 4 9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 3
1 4 9"""
        output = """81"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000 27 7
1 3 4 6 7 8 9"""
        output = """989112238"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000000000000000 29 6
1 2 4 5 7 9"""
        output = """853993813"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1000000000000000000 957 7
1 2 3 5 6 7 9"""
        output = """205384995"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, B, K = map(int, input().split(" "))
  C = [int(x) for x in input().split(" ")]

  

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
