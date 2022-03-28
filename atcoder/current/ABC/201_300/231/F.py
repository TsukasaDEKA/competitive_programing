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
50 100 150
1 3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
123456789 123456 123
987 987654 987654321"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
3 1 4 1 5 9 2 6 5 3
2 7 1 8 2 8 1 8 2 8"""
        output = """37"""
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
  from collections import Counter, defaultdict
  # 座標圧縮からのセグツリー
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  temp_b = sorted(list(set(B)))
  n_b = len(temp_b)

  comp_B = defaultdict(int)
  for i in range(n_b):
    comp_B[temp_b[i]] = i

  seg = SegTree([0]*n_b, segfunc, ide_ele)

  A_B = sorted([(A[i], B[i]) for i in range(N)])
  A_to_B = defaultdict(list)
  for i in range(N):
    a, b = A_B[i]
    A_to_B[a].append(b)

  for k in A_to_B.keys():
    A_to_B[k].sort()

  ans = 0
  used_A = set()

  for i in range(N):
    a, b = A_B[i]
    if a not in used_A:
      used_A.add(a)
      for b_ in A_to_B[a]:
        b_i = comp_B[b_]
        x = seg.query(b_i, b_i+1)
        seg.update(b_i, x+1)

    # b = A_to_B[a][0]
    b_i = comp_B[b]
    ans += seg.query(b_i, n_b)

  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()