#####segfunc#####
def segfunc(x, y):
  return max(x, y)
#################

#####ide_ele#####
# ide_ele = 0 # 区間和、最大公約数
# ide_ele = 1 # 区間積
# ide_ele = float('inf') # 最小値
ide_ele = - float('inf') # 最大値
#################

# 最大、最小の時しか上手く動かない。
class SegTreeWithIndex:
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
    self.indexes = [self.num] * 2 * self.num
    # 配列の値を葉にセット
    for i in range(n):
      self.tree[self.num + i] = init_val[i]
      self.indexes[self.num + i] = i
    # 構築していく
    for i in range(self.num - 1, 0, -1):
      self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
      if self.tree[i] == self.tree[2*i]:
        self.indexes[i] = self.indexes[2*i]
      else:
        self.indexes[i] = self.indexes[2*i+1]

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
      l, r = min(k, k ^ 1), max(k, k ^ 1)
      k >>= 1
      self.tree[k] = self.segfunc(self.tree[l], self.tree[r])
      if self.tree[k] == self.tree[l]:
        self.indexes[k] = self.indexes[l]
      else:
        self.indexes[k] = self.indexes[r]

  def query(self, l, r):
    """
    [l, r)のsegfuncしたものを得る
    l: index(0-index)
    r: index(0-index)
    """
    res = self.ide_ele
    index = r
    l += self.num
    r += self.num
    while l < r:
      # l & 1 => l が 奇数 (ペアの右側) だったら 1:
      if l & 1:
        if res == self.tree[l]:
          # 同値だったら小さい方のインデックスを取る。
          index = min(index, self.indexes[l])
          continue
        res = self.segfunc(res, self.tree[l])
        # この時点で self.tree[l] に書き換わったのが確定したので。
        if res == self.tree[l]:
          index = self.indexes[l]
        l += 1
      # r が奇数 = r-1 が偶数。なので、子のペアの左を見ることになる。
      if r & 1:
        if res == self.tree[r-1]:
          # 同値だったら小さい方のインデックスを取る。
          index = min(index, self.indexes[r-1])
          continue
        # この時点で self.tree[r-1] に書き換わったのが確定したので。
        res = self.segfunc(res, self.tree[r-1])
        if res == self.tree[r-1]:
          index = self.indexes[r-1]
      # l // 2
      l >>= 1
      r >>= 1
    return index, res


sample = list(range(16))
seg = SegTreeWithIndex(sample, segfunc, ide_ele)
print(seg.tree)

print(seg.indexes)
seg.update(10, 100)
print(seg.indexes)


# for i in range(len(sample)):
#   print(seg.query(1, i+1))