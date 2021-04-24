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
        input = """10 3
1
5
4
3
8
6
9
7
2
4"""
        output = """7"""
        self.assertIO(input, output)

#####segfunc#####
def segfunc(x, y):
  return max(x, y)
#################

#####ide_ele#####
ide_ele = 0
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
    k += self.num
    self.tree[k] = x
    while k > 1:
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
      if l & 1:
        res = self.segfunc(res, self.tree[l])
        l += 1
      if r & 1:
        res = self.segfunc(res, self.tree[r - 1])
      l >>= 1
      r >>= 1
    return res

def resolve():
  N, K = map(int, input().split(" "))
  max_range = (300000 + 1)
  dp = [0] * (max_range)
  seg = SegTree(dp, segfunc, ide_ele)

  for _ in range(N):
    A = int(input())
    left = max(A-K, 0)
    right = min(A+K+1, max_range) #半開区間なので +1 してる
    seg.update(A, seg.query(left, right) + 1)

  print(seg.query(0, max_range+1))

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
  unittest.main()
