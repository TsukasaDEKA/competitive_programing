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
        input = """3 3 2
1 2
5 4
9 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """9 4 1
1 5
2 4
3 3
4 2
5 1
6 2
7 3
8 4
9 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 0 1
300000000 1000000000
100000000 1000000000
200000000 1000000000"""
        output = """3000000000"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush
  # imos法のように処理する。
  # X の制約が <= 10**9 なので普通にやると間に合わない。
  # モンスター出現イベントと爆弾イベントで分けて考える。
  # モンスター出現イベントが発生した時に、そのモンスターを倒せるだけ爆弾を使う。
  # 爆弾の効果は 爆発した地点 X ~ X+2*D 先まで続くので X+2*D+0.1 にマイナス効果のイベントを発生させる。
  # X+2*D+1 にマイナス効果のイベントを入れて AC 取れてしまったけど、モンスター出現イベントと前後する危険があるので、
  # X+2*D+0.1 で計算するのが安心。
  # 上記で表記した「そのモンスターを倒せるだけ爆弾を使う。」とは具体的に、(Hi-<現在の爆弾効果> + A-1)//A 回爆弾を使うことである。
  # イベントの追加、取り出しが行われるので優先度付きキューを使えば良さそう。
  inf = 10**18+1
  N, D, A = map(int, input().split(" "))
  events = []
  for i in range(N):
    X, H = map(int, input().split(" "))
    heappush(events, (X, H))
  
  ans = 0
  bomb_power = 0
  while events:
    X, H = heappop(events)
    # H > 0 ならモンスター、H <= 0 は爆弾効果終了イベント
    if H > 0:
      if bomb_power >= H: continue
      times = (H-bomb_power+A-1)//A
      ans += times
      bomb_power += times*A
      heappush(events, (X+2*D+0.1, -(times*A)))
    else:
      bomb_power += H

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()