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
        input = """4 6
1 1 1 1 1 2
1 2 2 2 2 2
1 2 2 3 2 3
1 2 3 2 2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
1 2 3
4 5 6
7 8 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 3
7 7 7
7 7 7
7 7 7
7 7 7
7 7 7"""
        output = """15"""
        self.assertIO(input, output)

def resolve():
  # 愚直にやろうとすると O(H*W*(H*W)) とかになって間に合わない。
  # 計算量の削減について、以下のように考えた。
  # H <= 8 なので bit 演算するのが速そう
  # -> H 分の計算が減らせる。
  # ある数 X のみで構成される良い部分グリッドの大きさを計算するとき、
  # X を含まない列の情報は必要ないので座標圧縮みたいな事ができる
  # -> 1 <= Pij <= H*W なので高々 H*W 回の計算にできる
  # 以上の事から、以下の配列を作成して最後に集計する事で、高速に答えを出せる。
  # agg[i] = i が含まれる列の情報を「何行目に含まれるか」で bit 化した配列
  from collections import defaultdict

  H, W = map(int, input().split(" "))
  P = [[int(x) for x in input().split(" ")] for _ in range(H)]

  # P[h][w] を含む列の情報を集計。
  # defaultdict である必要はないけど、集計が楽になるので採用した。
  agg = [defaultdict(int) for _ in range(H*W)]
  for h in range(H):
    for w in range(W):
      agg[P[h][w]-1][w] += 1<<h

  ans = 0
  for i in range(H*W):
    # i が含まれる列の情報を「何行目に含まれるか」で bit 化した配列
    # 列の index は不要なので value だけの配列で扱う
    columns = agg[i].values()
    # 全ての行の選び方の組み合わせを試す。
    # bit : 選ばれた行を bit 表現した値。
    for bit in range(1, 1<<H):
      count = 0
      for column in columns:
        # 選ばれた行全てに i が含まれる列を数える。
        if bit&column == bit: count+=1
      if count == 0: continue

      # 良いグリッドの大きさ
      temp = bin(bit).count("1")*count
      if ans < temp: ans = temp

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()




