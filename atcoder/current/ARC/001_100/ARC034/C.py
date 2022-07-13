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
        input = """3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """15 4"""
        output = """2592"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """1000000 999900"""
    #     output = """21398499"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """1000000000 999999900"""
    #     output = """745508745"""
    #     self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  def factorization(n):
    arr = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
      if temp%i==0:
        while temp%i==0:
          arr[i]+=1
          temp //= i

    if temp!=1:
      arr[temp] = 1

    if arr.items()==[]:
      arr[n] = 1

    return arr

  # A-B の範囲が小さい ( <= 100 ) のでそれを利用したい。
  # A, B の約数列挙を毎回やっても O( sqrt(A) ) 程度の計算量しかかからない。
  # sqrt(A) <= 31623 程度なので間に合いそう。
  # 約数列挙をしてからどうする？
  # A! の約数は A, A-1, ... 2 の中から任意の数字を選んだものである。
  # この中で B! の倍数を考える。B! の倍数は B, B-1, B-2 ... の要素を全て含む。
  # つまり、A! の要素の中から B! の要素を全て選んだ上で、B+1 ~ A までの任意の要素を何個か選んだものは条件を満たす。
  # つまり、2**(A-B) 個の B の倍数が存在する。
  mod = 1000000007
  A, B = map(int, input().split(" "))

  facts = defaultdict(int)
  for a in range(B+1, A+1):
    for key, val in factorization(a).items():
      facts[key]+=val

  ans = 1
  for key, val in facts.items():
    if key == 1:continue
    ans*=val+1
    if ans >= mod: ans%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()