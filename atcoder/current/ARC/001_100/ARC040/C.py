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

    def test_入力例1(self):
        input = """7
...oooo
oo.....
ooooooo
ooooooo
.....oo
oooo...
ooooooo"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
.oo.
..oo
o..o
oo.."""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1
o"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = [input()[::-1] for _ in range(N)]

  ans = 0
  c = 0
  r = 0
  while r < N:
    while c < N:
      if S[r][c] == ".":
        ans+=1
        c+=1
        if c == N:
          c = 0
          r += 1
        break
      c+=1
    r += 1
    c %= N
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
