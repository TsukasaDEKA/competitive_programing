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
1144#
2233#"""
        output = """0.4444444444444444"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
9988#
1122#"""
        output = """1.0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
1122#
2228#"""
        output = """0.001932367149758454"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """100000
3226#
3597#"""
        output = """0.6296297942426154"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter
  K = int(input())
  S = Counter(list(map(int, list(input())[:4])))
  T = Counter(list(map(int, list(input())[:4])))
  # 100 パターン全部網羅すればいけそう
  # 残ったカードで全探索すると厳しそう。

  def score(n, hands):
    total = 0
    for i in range(1, 10):
      c = 0
      if i in hands: c+=hands[i]
      if i == n: c+=1
      total += i*pow(10, c)
    return total

  piles = [K]*10
  for s, val in S.items(): piles[s] -= val
  for t, val in T.items(): piles[t] -= val
  pile_amount = 9*K - 8

  win_count = 0
  for s in range(1, 10):
    if piles[s] == 0: continue
    # s を引く確率
    p_s = piles[s] / pile_amount
    for t in range(1, 10):
      if piles[t] == 0: continue
      if s == t and piles[s] <= 1: continue
      # t を引く確率
      if t == s: p_t = (piles[t]-1) / (pile_amount - 1)
      else: p_t = piles[t] / (pile_amount - 1)

      if score(s, S) > score(t, T):
        win_count+=p_s*p_t
  
  print(win_count)

resolve()

if __name__ == "__main__":
    unittest.main()
