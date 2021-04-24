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
        input = """4
0 1 2 3"""
        output = """0
3
4
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
0 3 1 5 4 2 9 6 8 7"""
        output = """9
18
21
28
27
28
33
24
21
14"""
        self.assertIO(input, output)

#####segfunc#####
def segfunc(x, y):
  return x+y
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
  # k = i の答えは k = i-1 の時の答えから簡単に求まる。
  # k = i-1 の時の先頭を X とした時に、X よりも小さい数字が X よりも後に X-1 個ある。
  # k = i の時にその X が末尾に来るので、X よりも大きい数字が X よりも前に N-X-2 個ある
  # つまり、f(k) を転倒数だとすると、
  # f(k) = f(k-1) - (X - 1) + (N - X - 2) = f(k-1) + N - 2*X - 1
  # f(k) を O(1) で求められるので、この部分の計算は f(1) ~ f(N-1) は O(N) で求められる。
  # 問題は k = 0 の時の転倒数を求める場合で、愚直に行うと O(N**2) になってしまう。
  # ここのオーダーを落としたい。
  # A を前から見ていった時に、今まで見たことがある数字がソートされていれば二分探索 O(logN) で求めることができる。
  # 中間挿入のコストがかかりそうだけど、試してみる。
  # -> ダメだった。
  # セグ木ならいけそう
  # => https://coonevo.hatenablog.com/entry/2020/03/19/174849#%E9%AB%98%E9%80%9F%E5%8C%96ONlogN

  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = SegTree([0]*N, segfunc, ide_ele)

  ans = 0
  # k = 0 の時の転倒数
  for i in range(N):
    ans+=i-B.query(0, A[i])
    B.update(A[i], 1)

  print(ans)
  for i in range(N-1):
    ans += N - 2*A[i] - 1
    print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
