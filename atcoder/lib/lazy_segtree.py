# 参考 => https://smijake3.hatenablog.com/entry/2018/11/03/100133
#####segfunc#####
def segfunc(x, y):
  return max(x, y)
#################

#####ide_ele#####
ide_ele = - float('inf')
#################

class LazySegTree:
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
    tree: セグメント木(0-index)
    lazy: 遅延評価用(0-index)
    lv: 深さ
    """
    n = len(init_val)
    self.segfunc = segfunc
    self.ide_ele = ide_ele
    self.lv = (n-1).bit_length()
    self.num = 1 << self.lv
    self.tree = [ide_ele] * 2 * self.num
    self.lazy = [None] * 2 * self.num
    # 配列の値を葉にセット
    for i in range(n):
      self.tree[self.num + i - 1] = init_val[i]
    # 構築していく
    for i in range(self.num-1, 0, -1):
      self.tree[i-1] = self.segfunc(self.tree[2*i-1], self.tree[2*i])

  def gindex(self, l, r):
    l += self.num
    r += self.num
    lm = (l // (l & -l)) >> 1
    rm = (r // (r & -r)) >> 1

    while l < r:
      if r <= rm: yield r
      if l <= lm: yield l
      l >>= 1
      r >>= 1
    while l:
        yield l
        l >>= 1

  # 1-indexedで単調増加のインデックスリストを渡す
  def propagates(self, *ids):
    for i in reversed(ids):
      v = self.lazy[i-1]
      if v is None: continue
      self.lazy[2*i-1] = self.tree[2*i-1] = self.lazy[2*i] = self.tree[2*i] = v
      self.lazy[i-1] = None

  def update(self, l, r, x):
    *ids, = self.gindex(l, r)
    # 1. トップダウンにlazyの値を伝搬
    self.propagates(*ids)
 
    # 2. 区間[l, r)のdata, lazyの値を更新
    l += self.num
    r += self.num

    while l < r:
      if r & 1:
        r -= 1
        self.lazy[r-1] = self.tree[r-1] = x
      if l & 1:
        self.lazy[l-1] = self.tree[l-1] = x
        l += 1
      l >>= 1; r >>= 1

    # 3. 伝搬させた区間について、ボトムアップにdataの値を伝搬する
    for i in ids:
      self.tree[i-1] = self.segfunc(self.tree[2*i-1], self.tree[2*i])

  # 区間[l, r)の最小値を求める
  def query(self, l, r):
    # 1. トップダウンにlazyの値を伝搬
    self.propagates(*self.gindex(l, r))
    l += self.num
    r += self.num

    # 2. 区間[l, r)の最小値を求める
    s = self.ide_ele
    while l < r:
      if r & 1:
        r -= 1
        s = self.segfunc(s, self.tree[r-1])
      if l & 1:
        s = self.segfunc(s, self.tree[l-1])
        l += 1
      l >>= 1; r >>= 1
    return s