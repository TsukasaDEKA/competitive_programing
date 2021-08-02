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
abcd
bcda
ada"""
        output = """Aoki
Takahashi
Draw"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
ABC"""
        output = """Draw"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
eaaaabaa
eaaaacaa
daaaaaaa
eaaaadaa
daaaafaa"""
        output = """Takahashi
Takahashi
Takahashi
Aoki
Takahashi"""
        self.assertIO(input, output)

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def resolve():
  # グラフ問題に帰着できそう。
  # 先頭 3 文字 => 末尾 3 文字の有向グラフ
  # 勝利条件は?
  # 最後に末端の文字を言えば良い。
  # 末端までの距離をそれぞれ集めていく。
  from collections import deque, defaultdict

  inf = 10**18+1
  N = int(input())
  S = [input() for _ in range(N)]
  EDGE = defaultdict(set)
  # REV = defaultdict(set)
  for i in range(N):
    EDGE[S[i][:3]].add(S[i][-3:])
    # REV[S[-3:]].add(S[:3])
  

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()