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
        input = """2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4"""
        output = """4"""
        self.assertIO(input, output)


    def test_入力例_3(self):
        input = """3 6"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1 100"""
        output = """50"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """1 3"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  H, W = map(int, input().split(" "))
  if H == 1 or W == 1:
    print(max(H, W))
    return
  print(((H+1)//2)*((W+1)//2))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
