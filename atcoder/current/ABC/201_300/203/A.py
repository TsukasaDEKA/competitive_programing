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
        input = """2 5 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter
  A = Counter([int(x) for x in input().split(" ")])

  if len(A.items()) == 3:
    print(0)
    return

  if len(A.items()) == 1:
    for key, val in A.items():
      print(key)
      return

  for key, val in A.items():
    if val == 1:
      print(key)
      return
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
