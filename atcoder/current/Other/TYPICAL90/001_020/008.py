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
        input = """10
attcordeer"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """41
btwogablwetwoiehocghiewobadegwhoihegnldir"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """140
aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr"""
        output = """279999993"""
        self.assertIO(input, output)

def resolve():
  # 深さ優先探索みたいに出来そう。
  # 答えが 10**9+7 以上を想定されてるので厳しそう。
  # 例えば前から見にいった時に、 t を見つけたら その前に a が何個あるか確認する。
  # そうすると、そこまで見にいった時に at となる部分列の個数がわかる。
  # それを繰り返していけば良さそう。
  mod = 10**9+7
  from collections import defaultdict

  N = int(input())
  S = list(input())
  atcoder = "atcoder"
  ans = defaultdict(int)
  for s in S:
    if s == "a":
      ans["a"] += 1
      continue

    i = atcoder.find(s)
    if i < 0: continue
    ans[atcoder[:i+1]] += ans[atcoder[:i]]

  print(ans[atcoder]%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

