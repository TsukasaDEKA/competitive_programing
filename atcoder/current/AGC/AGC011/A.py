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
        input = """5 3 5
1
2
3
6
12"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 3 3
7
6
2
8
10
6"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # T <= 10**9 なのでそのままやると厳しい。
  # N<=10**5 なので、「K 分経過するか C 人のった時点で出発する」みたいな方針でできそう。
  from collections import defaultdict
  N, C, K = map(int, input().split(" "))
  T = [int(input()) for x in range(N)]
  T_schedule = defaultdict(int)
  for t in T: T_schedule[t]+=1

  T_schedule = sorted([[key, value] for key, value in T_schedule.items()])

  ans = 0
  count = 0
  start_time = 0
  for time, amount in T_schedule:
    if count == 0: start_time = time
    if time > start_time + K:
      ans += 1
      count = 0
      start_time = time

    if count + amount >= C:
      ans += (count + amount)//C
      count = (count + amount)%C
      start_time = time
    else:
      count += amount
  if count: ans+=1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
