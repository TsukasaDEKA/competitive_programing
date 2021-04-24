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
        input = """3
6 5 1
1 10 1"""
        output = """12
11
0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
12 24 6
52 16 4
99 2 2"""
        output = """187
167
101
0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
12 13 1
44 17 17
66 4096 64"""
        output = """4162
4162
4162
0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  schedules = [[int(x) for x in input().split(" ")] for _ in range(N-1)]

  # 来た電車に乗る、というのを繰り返す。O(N**2) で N**2 <= 25*10**4 なので間に合うはず。
  for i in range(N-1):
    # i 番目の駅から出発する時にかかる時間を求める。
    ans = 0
    for schedule in schedules[i:]:
      c, s, f = schedule
      # 次の電車の出発時間を求める
      next_departure = s
      while next_departure < ans: next_departure += f
      ans = next_departure
      # 次の駅への到着時刻
      ans += c
    print(ans)
  # 最後の駅
  print(0)

resolve()

if __name__ == "__main__":
    unittest.main()
