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
        input = """3
1 2 2
1 2 3
1 2 4"""
        output = """2
-1
4"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())
  for _ in range(T):
    R, G, B = sorted([int(x) for x in input().split(" ")])
    if R == G or G == B:
      print(G)
      continue
    # 差が 3 の倍数であれば同値にできる。
    ans = inf
    if (G-R)%3 == 0:
      temp = (G-R)//3+G-(G-R)//3
      if ans > temp: ans = temp
    if (B-G)%3 == 0:
      temp = (B-G)//3+B-(B-G)//3
      if ans > temp: ans = temp
    if (B-R)%3 == 0:
      temp = (B-R)//3+B-(B-R)//3
      if ans > temp: ans = temp
    print(-1 if ans == inf else ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()