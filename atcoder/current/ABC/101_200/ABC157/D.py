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
        input = """4 4 1
2 1
1 3
3 2
3 4
4 1"""
        output = """0 1 0 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 10 0
1 2
1 3
1 4
1 5
3 2
2 4
2 5
4 3
5 3
4 5"""
        output = """0 0 0 0 0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 9 3
10 1
6 7
8 2
2 5
8 4
7 3
10 9
6 4
5 8
2 6
7 5
3 1"""
        output = """1 3 5 4 3 3 3 3 1 0"""
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
    return [(i, abs(x)) for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
def resolve():
  # 友達の友達の・・・の友達でまだ友達でなくてブロックもされてなかったら友達候補。
  # 2 人の選択パターンは N*(N+1)//2 <= 5*10**9 くらいなので全パターンチェックしてたら間に合わない。
  # 各人の友達リスト、ブロックリストを作る。
  # 友達関係で UnionFind して、同一 Union 内で検索すると早そう。
  # i さんの友達候補は、(i さんが所属する Union の人数 - 1) - i さんの友達 - i さんがブロックしている人の中で、Union に含まれている人の人数
  # O(N * log(N) + K + 構築コスト) なので間に合う。
  # ブロックリストを作成する時に、Union 内部でのブロックなのか、そうでないのかを先にチェックすると無駄計算を減らせる。
  N, M, K = map(int, input().split(" "))

  friends_group = UnionFind(N)
  friends_counts = [0]*N
  for _ in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    friends_group.union(A, B)
    friends_counts[A]+=1
    friends_counts[B]+=1

  block_counts = [0]*N
  for _ in range(K):
    C, D = [int(x)-1 for x in input().split(" ")]
    if friends_group.same(C, D):
      block_counts[C]+=1
      block_counts[D]+=1

  roots_size = [0]*N
  for root, size in friends_group.roots_with_size():
    roots_size[root] = size

  ans = [0]*N
  for i in range(N):
    ans[i] = max(roots_size[friends_group.find(i)] - 1 - friends_counts[i] - block_counts[i], 0)
  print(*ans)

resolve()

if __name__ == "__main__":
    unittest.main()
