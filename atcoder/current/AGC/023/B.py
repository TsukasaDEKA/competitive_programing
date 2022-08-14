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
        input = """2
ab
ca"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
aaaa
aaaa
aaaa
aaaa"""
        output = """16"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
abcde
fghij
klmno
pqrst
uvwxy"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 文字毎に集計を取ったらいけそう。
  # 1 種類の文字があった場合、その文字に関して条件を満たすことができるかどうかを考える。
  # 45 度回転に近い処理をする？
  # 全部を右or下方向にずらして、条件を満たしたら右下に 1 ~ N 個ズラしても条件を満たすはず。
  # なので、O(N**3) でいけるはず。

  N = int(input())
  S = [list(input()) for _ in range(N)]
  ans = 0
  for _ in range(N):
    S = S[1:]+S[0:1]
    # print(S)
    for i in range(N):
      for j in range(N):
        if S[i][j] != S[j][i]: break
      else: continue
      break
    else:
      ans+=N
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()