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
        input = """3
3 1 4
6 2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 1 1
1 1 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
5 4 1 3 2
5 4 1 3 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
8 5 4 7 4 5
10 5 6 7 4 1"""
        output = """7"""
        self.assertIO(input, output)

#####segfunc#####
def segfunc(x, y):
  return x+y
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
  from collections import defaultdict, deque
  inf = 10**18+1
  # 左に移動すると 1 増えて、右に移動すると 1 減る。
  # 毎回計算をやってると足りなさそう。
  # インデックス毎に集計を取っていくといける。
  # 最適なマッチング問題。
  # 端から動かしていく？
  # 移動回数のトータル - (前方へ移動する線と後方へ移動する線の交点の数) + (前方同士、後方同士の交点の数) が答え。
  # 例1 だと 4 - 2 + 0 = 2
  # 最初に移動回数を求める処理が大変そう。B[i] == A[i-k] になる最小の k を見つけるために O(N**2) かかる。
  # 愚直でもギリいける・・・？ => 無理っぽい。
  # 差を上手く使うと計算量を減らせたりする？
  N = int(input())
  if N == 3: return
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  # Ai+i をキューに入れて管理しておけば、マッチさせやすくなる。
  tar = defaultdict(deque)
  for i in range(N):
    A[i]+=i
    B[i]+=i
    tar[B[i]].append(i)

  s = [0]*N
  for i in range(N):
    if tar[A[i]]:
      s[i] = tar[A[i]].popleft()
    else:
      print(-1)
      return

  # この状態で転倒数を求める。
  # BIT?ってやつを使うと早いらしい。
  # セグ木でもいける。やってみる。
  ide_ele = 0
  seg = SegTree([0]*N, segfunc, ide_ele)
  # 転倒数
  tran = 0
  for i in range(N):
    tran += i - seg.query(0, s[i])
    seg.update(s[i], seg.query(s[i], s[i]+1)+1)

  print(tran)
import sys 
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
