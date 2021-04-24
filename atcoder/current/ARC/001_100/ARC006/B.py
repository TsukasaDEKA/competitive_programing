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
        input = """3 2
| |-|
|-| |
o"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
| |-| |-| |-| |-| |
|-| |-| |-| |-| |-|
            o"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 5
|
|
|
|
|
o"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4 2
| | | |
| | | |
      o"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """9 8
| | | | | | | | |
|-| | |-| | |-| |
| | |-| | |-| | |
| |-| | | | | |-|
| | | |-| | | |-|
| | |-| |-| | | |
|-| | |-| | |-| |
| | | | | |-| | |
            o"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # o から見ていって、上方向に辿っていく。
  # 両端の処理に注意
  N, L = map(int, input().split(" "))
  field = [list(input()) for _ in range(L)]
  mark = list(input())

  cursor = mark.index("o")
  for i in reversed(range(L)):
    if cursor-1 >= 0:
      if field[i][cursor-1] == "-":
        cursor-=2
        continue
    if cursor+1 < 2*N-1:
      if field[i][cursor+1] == "-":
        cursor+=2
  print(cursor//2+1)

resolve()

if __name__ == "__main__":
    unittest.main()
