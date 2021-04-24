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
        input = """7 26
NAOHIRO
ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 8
TAKOYAKI
TAKOYAKI"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 4
CHOKUDAI
MYON"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6 6
MONAKA
NAMAKO"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter
  _ = input()
  NAME = Counter(list(input()))
  KIT = Counter(list(input()))

  ans = 0
  for char, val in NAME.items():
    if char not in KIT:
      print(-1)
      return
    ans = max(ans, (val + KIT[char] - 1)//KIT[char])
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
