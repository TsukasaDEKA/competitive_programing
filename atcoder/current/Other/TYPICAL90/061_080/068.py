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
        input = """4
7
0 1 2 3
1 1 2 1
1 3 4 5
0 3 4 6
1 3 4 5
0 2 3 6
1 3 1 5"""
        output = """2
Ambiguous
1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """15
25
0 11 12 41
0 1 2 159
0 14 15 121
0 4 5 245
0 12 13 157
0 9 10 176
0 6 7 170
0 2 3 123
0 7 8 167
0 3 4 159
1 12 11 33
0 10 11 116
0 8 9 161
1 9 12 68
1 12 12 33
1 7 12 74
0 5 6 290
1 8 9 93
0 13 14 127
1 10 12 108
1 14 1 3
1 13 8 124
1 12 11 33
1 12 10 33
1 5 15 194"""
        output = """8
33
33
33
68
33
144
93
8
108
118"""
        self.assertIO(input, output)



class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def roots_with_size(self):
    return [(i, -x) for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

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
  # Q <= 10**5 なので 1 クエリに対して O(1) とか O(logN) くらいで処理したい。
  # 最後まで A の値は一意に定まることは無い。
  # その為、結論を得るまでにいくつかの値を跨ぐ必要がある場合が存在する点に注意する。
  # 例えば A1+A2 = 5, A2+A3 = 4, A3+A4 = 6 の時、 A1 = 2 だと仮定した時の A4 は？と言うクエリが来た時、
  # A2 = 3, A3 = 1, A4 = 5 のように 3 回の計算が必要になる。
  # これを愚直にやると最悪ケースで O(N**2) になって TLE になる。
  # どこかで計算を省略できないかを考える。
  # 例えば、A1+A2 = 5, A2+A3 = 4, A3+A4 = 6 の時、連立方程式を解けば
  # (A1+A2)-(A2+A3) = 5-4 なので A1-A3 = 1、(A1-A3)+(A3+A4) = 1+6 なので A1+A4 = 7 であり、
  # A1 = 2 だと仮定した時の A4 は 5 であると計算できる。
  # 一回の T=1 のクエリを処理した時に、その経路の計算結果を記録しておけば経路上の 2 点間のクエリは O(1) で求められるようになる。
  # 問題はそれをどのように実装するかという点にある。
  # N*N の二次元配列だと最大で 10**10 のデータが必要なので MLE する。
  # 
  # ここまで考えて構造的に Union-Find に似ていることに気が付く。
  # 例えば T = 0 クエリは Axi と Ayi を union する動作で、
  # 上記の連立方程式を解く計算は経路圧縮の動作になる。
  # また、Ambiguous になる条件は、Axi と Ayi の根が別々であることである。
  # 適当な Ai を根と定めて、そこからの差がどの程度なのかを決めておけば良さそう。
  # T=0 の時、Xi+1 = Yi であるという条件を使って何かできないか？
  # Xi+1 = Yi ということは、Axi, Axi+1, Axi+2 が 同一 Union だった場合、
  # 必ず Axi-Axi+2 の値がわかるということになる。
  # さらに考えると、同一 Union であれば偶数番目と奇数番目のお互いの距離がわかる。
  # 次回、その区間を通るときは O(1) で計算できる。
  # Union のタイミングで根からの距離 or 根+1 からの距離を記録しておけば
  # Union 同士の結合でも根からの距離を求められそうだけど、クエリ次第で計算量がかかりそうなので
  # やはり T=1 のクエリが来たタイミングで更新するか。
  # T, X, Y, V = 1, 4, 8, 2 のクエリが来たとして、

  N = int(input())
  Q = int(input())
  uf = UnionFind(N)
  seg = SegTree([0]*(N-1), segfunc, ide_ele)
  for _ in range(Q):
    T, X, Y, V = [int(x) for x in input().split(" ")]
    X-=1
    Y-=1
    if T==0:
      uf.union(X, Y)
      if X%2==0: V *= -1
      seg.update(X, V)
    else:
      if uf.same(X, Y):
        temp = seg.query(min(X, Y), max(X, Y))
        # 演算の回数で V の反転回数が決まるので X-Y の偶奇で場合分する。
        if (X-Y)%2: V *= -1
        # 演算向きの前後と答えになるインデックスの偶奇を比較して、一致していたら差を取って、そうで無いなら和をとる。
        # なぜそうなるかがよくわかってない。
        if int(X <= Y) == Y%2:temp*=-1
        print(V+temp)        
      else:
        print("Ambiguous")

# 色々試した結果、 int(X <= Y) != Y%2 の時に temp を反転させると良さそう。なんで？
# ↓ V+temp の時に正しい答えが出る。
# 1 0 1 1 1 0 -93 161 7 8
# 1 0 1 0 0 1 -124 217 12 7
# 0 0 0 1 0 0 194 -76 4 14
# 0 1 1 0 1 1 33 75 11 9

# ↓ V-temp の時に正しい答えが出る。
# 1 1 0 0 1 0 -33 -41 11 10
# 1 1 0 0 1 0 -3 -147 13 0
# 1 1 0 1 0 1 -68 -101 8 11
# 0 1 1 1 1 1 33 0 11 11
# 1 1 0 1 0 1 -74 -107 6 11
# 0 1 1 1 1 1 108 75 9 11

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
