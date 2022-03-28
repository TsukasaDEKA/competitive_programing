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

#####ide_ele#####
ide_ele = 0 # 区間和、最大公約数
# ide_ele = 1 # 区間積
# ide_ele = float('inf') # 最小値
# ide_ele = - float('inf') # 最大値
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
  from collections import defaultdict

  # 右に x 移動すると +x される。
  # 左に x 移動すると -x される。
  # A, B の各数字に対して +index してみて、同じ数字であれば一致させられる。
  # 同じ数字の組み合わせをそれぞれ並べた時、A, B のそれぞれの並び順でマッチさせるのが最も手数が少なくなる。
  # これで A の特定の数字を最終的に到達させたいインデックスがもとまった。
  # そのインデックスは順列になっており、そのインデックスを並べ変えて 1...N にするための手数を求めたい。
  # これは転倒数と一致するはず。
  # 転倒数は seg tree で簡単に求めることができる。
  N = int(input())
  A = [i+int(x) for i, x in enumerate(input().split(" "))]
  B = [i+int(x) for i, x in enumerate(input().split(" "))]
  aggA = defaultdict(list)
  aggB = defaultdict(list)
  for i in range(N):
    aggA[A[i]].append(i)
    aggB[B[i]].append(i)

  # A[i] が最終的に移動すべきインデックスを記録する。
  convertedA = [0]*N
  for key in aggA.keys():
    if len(aggA[key]) != len(aggB[key]):
      print(-1)
      return
    for a, b in zip(aggA[key], aggB[key]):
      convertedA[a] = b

  # 転倒数を求める。
  ans = 0
  seg = SegTree([0]*N, segfunc, ide_ele)
  for i in range(N):
    ans += seg.query(convertedA[i], N)
    seg.update(convertedA[i], 1)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()