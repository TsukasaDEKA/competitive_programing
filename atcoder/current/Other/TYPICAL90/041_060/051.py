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
        input = """5 2 10
3 8 7 5 11"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1 10
7 7 7 7 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """40 20 100
1 3 1 3 4 1 3 5 5 3 3 4 1 5 4 4 3 1 3 4 1 3 2 4 4 1 5 2 5 3 1 3 3 3 5 5 5 2 3 5"""
        output = """137846528820"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 1 10
7 7"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  # bit DP かなー
  # N, K が小さい。
  # 40C20 = 137,846,528,820	なので、全探索は厳しい。
  # DFS で途中でPを超えたら打ち切るとかするか。
  # 大きい方から取ってって、P を超過しなかったら全組み合わせでいける。
  # bit で考える。例えば N = 6, K = 3 の場合、商品が値段で昇順に並べられていた場合、小さい方から二分探索していくことができる？
  # 同値の商品があると、小さい方から並べるのは容易じゃない。
  # 深さ優先探索をしていく。
  # 前に取ったビット以降の bit をとるようにすれば重複がない。
  from collections import defaultdict
  N, K, P = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  B = [x for x in A[N//2:]]
  A = [x for x in A[:N//2]]
  dist_A = defaultdict(list)
  dist_B = defaultdict(list)
  for i in range(2**len(A)):
    count = bin(i).count("1")
    temp = 0
    for j in range(len(A)):
      if i>>j&1: temp+=A[j]
    if temp > P: continue
    dist_A[count].append(temp)

  for i in range(2**len(B)):
    count = bin(i).count("1")
    temp = 0
    for j in range(len(B)):
      if i>>j&1: temp+=B[j]
    if temp > P: continue
    dist_B[count].append(temp)
  
  for i in range(len(B)):
    dist_A[i].sort()
    dist_B[i].sort()

  # メグル式二分探索。
  def binary_search(ok, ng, solve, target, base):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, target, base): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, target, base) else -1

  def solve(x, target, base):
    return target[x] <= base

  ans = 0
  for i in range(min(K, len(B)) + 1):
    if len(dist_A[i])==0: continue
    if len(dist_B[K-i])==0: continue
    for a in dist_A[i]:
      b = P - a
      ok = 0
      ng = len(dist_B[K-i])
      count = binary_search(ok, ng, solve, dist_B[K-i], b)
      ans += count+1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
