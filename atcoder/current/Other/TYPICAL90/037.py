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
        input = """100 4
30 40 120
30 40 30
30 40 1500
30 40 40"""
        output = """1660"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 4
13 15 31415
12 13 92653
29 33 58979
95 98 32384"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5000 5
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000
1000 1000 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10000 20
4539 6002 485976
1819 5162 457795
1854 2246 487643
1023 4733 393530
1052 6274 289577
1874 2436 167747
1457 4248 452660
2103 4189 174955
3057 5061 319316
4898 4953 394627
1313 2880 154687
1274 1364 259598
3866 5844 233027
1163 5036 386223
1234 4630 155972
2845 4978 442858
3168 5368 171601
3708 4407 394899
3924 4122 428313
2112 4169 441976"""
        output = """2727026"""
        self.assertIO(input, output)

#####segfunc#####
def segfunc(x, y):
  return max(x, y)
#################

#####ide_ele#####
# ide_ele = 0 # 区間和、最大公約数
# ide_ele = 1 # 区間積
# ide_ele = float('inf') # 最小値
ide_ele = 0 # 最大値
#################

class SegTree:
  """
  init(init_val, ide_ele): 配列init_valで初期化 O(N)
  update(k, x): k番目の値をxに更新 O(logN)
  query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
  """
  def __init__(self, init_val, segfunc, ide_ele):
    """
    init_val: 配列の初期値
    segfunc: 区間にしたい操作
    ide_ele: 単位元
    n: 要素数
    num: n以上の最小の2のべき乗
    tree: セグメント木(1-index)
    """
    n = len(init_val)
    self.segfunc = segfunc
    self.ide_ele = ide_ele
    self.num = 1 << (n - 1).bit_length()
    self.tree = [ide_ele] * 2 * self.num
    # 配列の値を葉にセット
    for i in range(n):
      self.tree[self.num + i] = init_val[i]
    # 構築していく
    for i in range(self.num - 1, 0, -1):
      self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

  def update(self, k, x):
    """
    k番目の値をxに更新
    k: index(0-index)
    x: update value
    """
    # 葉の部分が前半に入っている。+= self.numをすることで元になる配列要素に移動
    k += self.num
    self.tree[k] = x
    while k > 1:
      # k >> 1 == k // 2 (index k の親の index)
      # k ^ 1 : 末尾を xor する。偶数だったら +1、奇数だったら -1 する。k インデックス(子)の片割れ
      self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
      k >>= 1

  def query(self, l, r):
    """
    [l, r)のsegfuncしたものを得る
    l: index(0-index)
    r: index(0-index)
    """
    res = self.ide_ele

    l += self.num
    r += self.num
    while l < r:
      # l & 1 => l が 奇数 (ペアの右側) だったら 1:
      if l & 1:
        res = self.segfunc(res, self.tree[l])
        l += 1
      # r が奇数 = r-1 が偶数。なので、子のペアの左を見ることになる。
      if r & 1:
        res = self.segfunc(res, self.tree[r - 1])
      # l // 2
      l >>= 1
      r >>= 1
    return res

def resolve():
  inf = 10**18+1
  # 香辛料の量で DP。
  # dp[i][w] =: i 番目までの料理を使った時の価値の最大値
  # 1 番目の料理を作った時に、Li ~ Ri までの最大値 + Vi すれば良い。
  # i 番目の料理の情報は必要か？ => 要らなさそう。
  # 最大値を区間で更新していけば良いので、セグ木上でやれば上手く行きそう。
  W, N = map(int, input().split(" "))
  seg = SegTree([0]*(W+1), segfunc, ide_ele)
  max_w = 0
  for i in range(N):
    l, r, v = map(int, input().split(" "))
    # 0 は常に 0 にしておきたい。
    for w in reversed(range(max(1, l), min(max_w+r, W)+1)):
      max_v = seg.query(max(0, w-r), w-l+1)
      if max_v <= 0 and w-r > 0: continue
      max_v += v
      current = seg.query(w, w+1)
      max_w = max(max_w, w)
      if current > max_v: continue
      seg.update(w, max_v)

  ans = seg.query(W, W+1)
  if ans == 0:
    print(-1)
    return
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
