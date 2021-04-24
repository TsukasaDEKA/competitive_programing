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
        input = """5 100 90 80
98
40
30
21
80"""
        output = """23"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 100 90 80
100
100
90
90
90
80
80
80"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 1000 800 100
300
333
400
444
500
555
600
666"""
        output = """243"""
        self.assertIO(input, output)

def resolve():
  # N <= 8 でものすごく小さい。
  # N 本ある竹を適切に割り振った後に伸び縮みさせた時にどれくらいのコストがかかるか
  # 組み合わせパターンがいくつあるのか考える。
  # 竹の並び替えパターンは N! で、間は N-1 個あって、その間を 2 個選ぶと考えると、
  # N! * (N-1)C2 で、 N=8 の時、N! * (N-1)C2 = 846720 なので間に合いそう。
  # 使わない竹があってもいいって事を忘れてた。ダメかも。
  # 一番長さが近い竹を貪欲に取っていく方法だと・・・ダメ
  # 1000, 1000, 1000 を作るのに、
  # L = 950, 300, 400, 300, 1000, 1200 だと、300+400+300 のケースを見逃してしまう。
  # ぴったりが当てはまる場合はそれを当てはめていくと良い？
  # 3 本作ってみて列挙するのがいいのかなぁ。
  # 竹の並び替え全パターンに対して、<A|B|C|使わない竹> という区切り方で全探索する。
  # 竹の間 + 末尾は N 個あるので、区切り方は NC3 で N=8 の時に NC3 = 56、
  # 全体の計算が 8!*56 = 2257920 なのでまぁ間に合いそう。
  from itertools import permutations
  inf = 10**18+1
  N, A, B, C = map(int, input().split(" "))
  L = [int(input()) for _ in range(N)]

  ans = inf
  for per in permutations(list(range(N))):
    sum_L = [0]*(N+1)
    for i in range(N):
      sum_L[i+1] = sum_L[i] + L[per[i]]

    for a in range(1, N-1):
      if ans == 0: break
      A_ = sum_L[a]
      for b in range(a+1, N):
        if ans == 0: break
        B_ = sum_L[b] - sum_L[a]
        for c in range(b+1, N+1):
          if ans == 0: break
          C_ = sum_L[c] - sum_L[b]
          temp = abs(A-A_)+abs(B-B_)+abs(C-C_)+10*(c-3)
          if temp < ans:
            ans = temp

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
