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
        input = """3 4
4 3
4 1
2 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3
1 2
1 3
1 4
2 1
2 3"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1
2 1"""
        output = """0"""
        self.assertIO(input, output)

#####segfunc#####
def segfunc(x, y):
  return min(x, y)
#################

#####ide_ele#####
ide_ele = 10**18+1
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
      # l & 1 == l が 奇数だったら 1:
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
  # A が M 以下のバイトを一つ、 A が M-1 以下のバイトを一つ、 A が M-2 以下のバイトを一つ・・・
  # といった風に選べる。
  # 報酬が高い順にそのバイトが選べるかどうかを判定していく。
  # 計算量が厳しいかも
  # 最悪 N*M の計算量がかかるので、N*M が大きいと間に合わない。
  # 区間の最小値を出すので、セグ木の応用でいけるか？
  # 使ったら inf に書き換えれば良い。
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  DATA = sorted([list(map(int, input().split(" "))) for _ in range(N)], key=lambda x: x[1], reverse=True)
  seg = SegTree(list(range(M+1)), segfunc, ide_ele)

  ans = 0
  for a, b in DATA:
    i = seg.query(a, M+1)
    if i != inf:
      seg.update(i, inf)
      ans += b
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
