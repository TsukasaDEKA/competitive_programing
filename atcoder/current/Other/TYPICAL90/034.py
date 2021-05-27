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
        input = """5 1
1 2 3 4 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4
1 1 2 4 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 2
1 2 3 4 4 3 2 1 2 3"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  # 全探索すると N**2 コストがかかる。
  # 1 <= ai <= 10**9 なので、bit 表現だと厳しい。
  # 含まれている要素の数は増えることはあっても減ることは無い。
  # 尺取でいけそう。
  from collections import defaultdict
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  # 一旦 r を K+1 まで動かして、
  count = defaultdict(int)
  count[A[0]] += 1
  total = set()
  total.add(A[0])
  l = 0
  r = 0
  ans = 1
  while l < N and r < N:
    # r を K を超えない範囲で進めていく。
    while len(total) <= K:
      if r + 1 >= N: break
      if len(total) == K and A[r+1] not in total and count[A[r+1]] == 0:
        break
      r += 1
      total.add(A[r])
      count[A[r]] += 1

    # 答えを更新
    ans = max(ans, r - l + 1)

    # l を一つ進める。
    count[A[l]] -= 1
    if count[A[l]] == 0:
      total.discard(A[l])
    l+=1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
