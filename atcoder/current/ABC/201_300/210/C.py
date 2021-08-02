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
        input = """7 3
1 2 1 2 3 3 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
4 4 4 4 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 6
304621362 506696497 304621362 506696497 834022578 304621362 414720753 304621362 304621362 414720753"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
  from collections import defaultdict
  # 最初に C[0:K] のアメを手元に取って色の種類数を調べる。
  # C[1:K+1] にした時に色の種類数が変化するのでそれをシミュレートする。
  # C[N-K:N] までシミュレートして、色の種類数が最大になった時の値を出力する。
  N, K = map(int, input().split(" "))
  C = [int(x) for x in input().split(" ")]

  # candies[i] : i 色のキャンディが現在手元に何個あるか
  # 1 <= C[i] <= 10**9 なので配列で実装すると MLE するか、メモリ確保に時間がかかって TLE する。
  candies = defaultdict(int)

  # 手元にあるキャンディの色の種類数
  colors = ans = 0
  for i in range(N):
    # i-K 番目のアメを手元から列に戻す動作。
    if i-K >= 0:
      candies[C[i-K]]-=1
      if candies[C[i-K]] == 0:
        colors-=1

    # i 番目のアメを列から手元に取ってくる動作。
    candies[C[i]]+=1
    if candies[C[i]] == 1:
      colors+=1

    ans = max(ans, colors)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()