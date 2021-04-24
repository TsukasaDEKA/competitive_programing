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

    def test_Sample_Input_1(self):
        input = """2 3 3
2 2
1 1
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 4
3 3
3 1
1 1
1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5 10
2 5
4 3
2 3
5 5
2 2
5 4
5 3
5 1
3 5
1 4"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # H, W < 3*10**5 なので全ての点に対して処理を行うとTLE。
  # 爆破対象だけみる。
  # h, w をそれぞれ集計して、合計の最大値をとる。
  # ans = (h_a, w_a) の時、爆破できる対象は h_a == h or w_a == w になる点である。
  # 爆破対象を最大化したい。
  # h, w を別々に集計すると、h_a == h and w_a == w のパターンで 2 回カウントされてしまう。

  H, W, M = map(int, input().split(" "))
  h_count = defaultdict(int)
  w_count = defaultdict(int)
  max_h = 0
  max_w = 0

  # 爆弾の設置点に爆破対象があった場合を考えて、爆破対象を確認できるようにしとく。
  targets = set()
  for _ in range(M):
    h, w = map(int, input().split(" "))
    targets.add((h, w))
    h_count[h]+=1
    w_count[w]+=1
    max_h = max(max_h, h_count[h])
    max_w = max(max_w, w_count[w])

  # h の出現回数が最大値のものだけ集める
  max_h_set = set()
  for h, h_val in h_count.items():
    if h_val == max_h: max_h_set.add(h)

  # w の出現回数が最大値のものだけ集める
  max_w_set = set()
  for w, w_val in w_count.items():
    if w_val == max_w: max_w_set.add(w)

  # print(max_h_set)
  # print(max_w_set)
  # h の出現回数が最大値のものと w の出現回数が最大値のものの組み合わせの中で、(h, w) に爆破対象が無いものを探す。
  # 全部の組み合わせをチェックしてみて、もし全てに爆破対象があるならば max_h+max_w-1 が答え。
  # 組み合わせの中で、(h, w) に爆破対象が無い物が見つかれば、そこに爆弾を置いた時に max_h+max_w 個破壊できる。
  # ちょっとわかりにくいけど、targets の個数+1個以上には処理しないので、max_h_set と max_w_set の数が多くても大丈夫
  ans = max_h + max_w
  for h in max_h_set:
    for w in max_w_set:
      if (h, w) not in targets:
        print(ans)
        return
  print(ans - 1)

resolve()

if __name__ == "__main__":
    unittest.main()
