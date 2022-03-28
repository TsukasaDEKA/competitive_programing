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

    def test_Sample_Input_1(self):
        input = """5 3
2 1 6 3 1"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 1000000000000
260522 914575 436426 979445 648772 690081 933447 190629 703497 47202"""
        output = """826617499998784056"""
        self.assertIO(input, output)

def resolve():
  # グラフの問題っぽい。
  # K > N の場合、絶対に閉路が存在するので、シミュレーションは閉路の手前までで良い。
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  mod_A = [x%N for x in A]
  count = [0]*N
  count[0] = 1
  if K <= N:
    ans = 0
    index = 0
    for _ in range(K):
      ans += A[index]
      index += mod_A[index]
      if index >= N: index%=N
    print(ans)

  else:
    # 一旦閉路を見つけるまでやる。
    ans = 0
    step = [-1]*N
    step[0] = 0
    index = 0
    next_ = 0
    length = 1
    k = K
    for _ in range(k):
      K -= 1
      ans += A[index]
      next_ = index+mod_A[index]
      if next_>=N: next_%=N
      if step[next_] >= 0:
        break
      step[next_] = step[index]+1
      index = next_

    length = step[index] - step[next_] + 1
    loop = K//length
    dist = K%length
    for _ in range(length):
      index = next_
      ans += A[index]*loop
      next_ = index+mod_A[index]
      if next_>=N: next_%=N
      index = next_

    for _ in range(dist):
      index = next_
      ans += A[index]
      next_ = index+mod_A[index]
      if next_>=N: next_%=N
      index = next_
    print(ans)
    return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()