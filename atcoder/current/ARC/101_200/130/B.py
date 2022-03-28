import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """4 5 6 5
1 1 6
1 3 3
2 2 4
2 4 2
1 1 2"""
        output = """0 8 3 3 0 0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 1000000000 3 5
1 1 2
1 2 2
1 3 2
1 4 2
1 5 2"""
        output = """0 5000000000 0"""
        self.assertIO(input, output)

def resolve():
  # 逆順に塗ってくと楽そう。
  inf = 10**18+1
  H, W, C, Q = map(int, input().split(" "))
  QUERY = reversed([[int(x)-1 for x in input().split(" ")] for _ in range(Q)])
  used_column = set()
  used_row = set()
  ans = [0]*C
  for t, n, c in QUERY:
    if t == 0:
      if n in used_row: continue
      used_row.add(n)
      ans[c]+=W-len(used_column)
    else:
      if n in used_column: continue
      used_column.add(n)
      ans[c]+=H-len(used_row)
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()