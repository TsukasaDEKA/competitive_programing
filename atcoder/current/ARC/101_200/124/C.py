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
        input = """2
2 15
10 6"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
148834018 644854700
947642099 255192490
35137537 134714230
944287156 528403260
68656286 200621680"""
        output = """238630"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20
557057460 31783488
843507940 794587200
640711140 620259584
1901220 499867584
190122000 41414848
349507610 620259584
890404700 609665088
392918800 211889920
507308870 722352000
156850650 498904448
806117280 862969856
193607570 992030080
660673950 422816704
622015810 563434560
207866720 316871744
63057130 117502592
482593010 366954816
605221700 705015552
702500790 900532160
171743540 353470912"""
        output = """152594452160"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2
72 10
40 45"""
        output = """90"""
        self.assertIO(input, output)

def make_divisors(n):
  lower_divisors, upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]

def resolve():
  from math import gcd
  def lcm(x, y):
    return (x * y) // gcd(x, y)
  # 必ずカードは別れる。
  # 組み合わせパターンは最大 2**50 なので、愚直にやると間に合わ無い。
  # 赤い袋の GCD が X、青い袋の GCD が Y になる条件は
  # 全てのパックの中に X の倍数と Y の倍数がそれぞれ含まれている必要がある。
  # ありえる全ての X と Y の組みをチェックするのは時間がかかるが、
  # 1 パック目の 2 枚のカードのそれぞれの約数の組み合わせを全探索することである程度高速に処理できる。
  N = int(input())
  PACK = [[int(x) for x in input().split(" ")] for _ in range(N)]
  divisors = [[0]*2 for _ in range(N)]

  for i in range(N):
    divisors[i][0] = set(make_divisors(PACK[i][0]))
    divisors[i][1] = set(make_divisors(PACK[i][1]))

  ans = 0
  for dr in divisors[0][0]:
    for db in divisors[0][1]:
      if lcm(dr, db) <= ans: continue
      for i in range(1, N):
        if (dr in divisors[i][0] and db in divisors[i][1]) or (dr in divisors[i][1] and db in divisors[i][0]): continue
        break
      else:
        ans = max(ans, lcm(dr, db))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()