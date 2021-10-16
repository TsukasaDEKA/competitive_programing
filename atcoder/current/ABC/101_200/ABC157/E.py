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
        input = """7
abcdbbd
6
2 3 6
1 5 z
2 1 1
1 4 a
1 7 d
2 1 7"""
        output = """3
1
5"""
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
  alpha2num = lambda c: ord(c) - ord('a')
  inf = 10**18+1
  N = int(input())
  S = list(input())
  Q = int(input())
  # 区間内に含まれる文字の個数を管理する
  # 各文字毎にセグツリーを持っておくとよさそう。
  # print
  letters = [SegTree( [0]*N, segfunc, ide_ele) for _ in range(26)]
  # 初期化
  for i in range(N):
    letters[alpha2num(S[i])].update(i, 1)

  for _ in range(Q):
    query = input().split(" ")
    if query[0] == "1":
      _, i, c = query
      i = int(i)-1
      if c == S[i]: continue
      old = S[i]
      new = S[i] = c
      letters[alpha2num(old)].update(i, 0)
      letters[alpha2num(new)].update(i, 1)
    else:
      _, l, r = [int(x)-1 for x in query]
      ans = 0
      for j in range(26):
        if letters[j].query(l, r+1): ans+=1
      print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()