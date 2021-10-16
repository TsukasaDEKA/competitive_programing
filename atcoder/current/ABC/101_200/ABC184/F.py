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
#         input = """5 17
# 2 3 5 7 11"""
#         output = """17"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """40 17
2 3 5 7 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 17"""
        output = """17"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """6 100
# 1 2 7 5 8 10"""
#         output = """33"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """6 100
# 101 102 103 104 105 106"""
#         output = """0"""
#         self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """7 273599681
# 6706927 91566569 89131517 71069699 75200339 98298649 92857057"""
#         output = """273555143"""
#         self.assertIO(input, output)

def resolve():
  # 半全列挙する。
  # 前半を列挙してソートしておく。
  # 後半を列挙した時に合計値が T 以下かつ最大となる組み合わせは O(log N) で求まる。
  # ソートがボトルネックになって全体計算量は O(NlogN) になる。
  # bit DP は必要かなー
  from bisect import bisect_left

  inf = 10**18+1
  N, T = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  max_head_size = 20
  # N が小さい時の場合分けが大変なので、N <= 20 の場合は全探索する。
  head = set()
  for bit in range(1<<min(N, max_head_size)):
    t = 0
    for i in range(min(N, max_head_size)):
      if bit&(1<<i): t+=A[i]

    if t <= T: head.add(t)
  head = sorted(list(head))

  if N <= max_head_size:
    print(head[-1])
  else:
    ans = 0
    tail_size = N-max_head_size
    A = A[max_head_size:]
    for bit in range(1<<tail_size):
      t = 0
      for i in range(tail_size):
        if bit&(1<<i): t+=A[i]

      if t <= T:
        # ここの実装をちょっと考える。
        # head の中で T-t 以下の数字の最大値を探す。
        i = bisect_left(head, T-t)
        if head[min(i, len(head)-1)] == T-t:
          print(T)
          return
        if i-1 >= 0:
          ans = max(ans, t+head[i-1])
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()