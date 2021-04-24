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

    def test_入力例1(self):
        input = """10 1
100 200 300 400 500 600 700 800 900 1000
1000 3 1 2 3"""
        output = """6100"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """12 10
1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000 1000
1000 4 1 2 4 7
1000 4 1 9 11 12
1000 4 3 5 8 9
1000 4 6 10 11 12
1000 4 2 4 7 10
1000 4 1 8 9 10
1000 3 1 9 12
1000 4 3 8 11 12
1000 4 1 2 3 4
1000 4 7 8 9 10"""
        output = """19000"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """13 8
328 781 104 102 132 108 100 102 104 108 168 102 100
184 4 10 11 3 4
190 4 9 6 2 5
282 6 9 1 3 12 10 8
205 8 13 10 1 12 7 2 8 11
122 8 13 5 4 3 8 9 12 10
112 7 11 6 12 8 2 13 5
102 4 4 13 6 12
109 6 7 2 13 1 8 6"""
        output = """3239"""
        self.assertIO(input, output)

def resolve():
  from itertools import combinations
  # bit DP か？
  # 9 人選ぶのは固定。
  # 16C9 = 11,440 なので、計算量的には問題なさそう。
  # M <= 50 で C <= N <= 16 なので、50*16*16C9 = 9152000 < 10**7

  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  combo = [list(map(int, input().split(" "))) for _ in range(M)]

  ans = 0
  members = combinations(list(range(N)), 9)
  for member in members:
    score = 0
    member = set(member)
    for m in member:
      score += A[m]
    for C in combo:
      count = 0
      for i in C[2:]:
        if i-1 in member: count += 1
        if count >= 3:
          score+=C[0]
          break
    ans = max(ans, score)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
