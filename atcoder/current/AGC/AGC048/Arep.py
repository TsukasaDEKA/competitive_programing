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
        input = """4
atcodeer
codeforces
aaa
aaab"""
        output = """1
0
-1
3"""
        self.assertIO(input, output)

def resolve():
  # -1, 0, 1 の 3 パターンしかない。(はず)
  # a しか含まれないパターンは -1
  # 既に atcoder より大きい場合は 0 回
  # それ以外は 1
  N = int(input())
  for _ in range(N):
    S = input()
    if S > "atcoder":
      print(0)
      continue 

    S = list(S)
    for i in range(len(S)):
      # 最初に見つかった a 以外のインデックス
      if S[i] != "a":
        if S[i] > "t": i-=1
        print(i)
        break
    else:
      # a しか含まれないパターン
      print(-1)
      continue

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()