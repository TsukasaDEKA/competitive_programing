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
        input = """a
abcdefgabcdefg"""
        output = """bcdefgbcdefg"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """g
aassddffgg"""
        output = """aassddff"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """a
aaaaa"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """l
qwertyuiopasdfghjklzxcvbnm"""
        output = """qwertyuiopasdfghjkzxcvbnm"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """d
qwsdtgcszddddsdfgvbbnj"""
        output = """qwstgcszsfgvbbnj"""
        self.assertIO(input, output)

def resolve():
  X = input()
  S = input()

  for s in S:
    if s!=X: print(s, end="")

  print()

resolve()

if __name__ == "__main__":
    unittest.main()
