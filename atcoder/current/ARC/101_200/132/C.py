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

#     def test_Sample_Input_1(self):
#         input = """4 2
# 3 -1 1 -1"""
#         output = """2"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """5 1
# 2 3 4 5 -1"""
#         output = """0"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """16 5
# -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"""
#         output = """794673086"""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4 2
-1 -1 -1 -1"""
        output = """12"""
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
  mod = 998244353
  # 枠の数を管理する。
  inf = 10**18+1
  N, D = map(int, input().split(" "))
  A = [int(x)-1 for x in input().split(" ")]
  data = [1 if x < 0 else 0 for x in A]
  seg = SegTree(data, segfunc, ide_ele)

  used = set(A)
  target = []
  for i in range(N):
    if i not in used:
      target.append(i)

  for i in range(N):
    if abs(A[i]-i) > D and A[i] >= 0:
      print(0)
      return 
  
  ans = 1
  for t in target:
    l, r = max(0, t-D), min(N-1, t+D)+1
    if seg.query(l, r) > 0:
      val = seg.query(l, r)
      print(l, r, t, val)
      ans*=val
      val = seg.query(r-1, r)
      seg.update(r-1, val-1)
    else:
      # print("hoge")
      print(0)
      return
    if ans >= mod: ans %= mod
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()