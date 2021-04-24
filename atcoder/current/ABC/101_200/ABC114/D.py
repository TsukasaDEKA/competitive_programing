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
        input = """9"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100"""
        output = """543"""
        self.assertIO(input, output)

def resolve():
  # 100 までなので、全部素因数分解しても大丈夫。
  # 75 = 3*5*5 なので、素因数の個数が 2, 4, 4 となる数字をどれくらい作れるかを調べる。
  # 例えば結果が {2: 8, 3: 4, 5: 2, 7: 1} となった時、{2: 4, 3: 4, 5: 2} = 32400 だけが七五数であることがわかる。
  # 100! を素因数分解した時に、2 が 97 個含まれる。2**74 の約数は 75 個なのでこれも 七五数。
  # 4,4,2 ・ 14,4 ・ 24,2 ・ 74 のそれぞれのパターンを考える必要がある。
  N = int(input())
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

  count = defaultdict(int)
  for i in range(2, N+1):
    facts = factorization(i)
    for key, val in facts.items():
      count[key]+=val 
 
  over_2 = over_4 = over_14 = over_24 = over_74 = 0
  for val in count.values():
    if val >= 2: over_2+=1
    if val >= 4: over_4+=1
    if val >= 14: over_14+=1
    if val >= 24: over_24+=1
    if val >= 74: over_74+=1

  from scipy.special import comb
  ans = comb(over_2-2, 1, exact=True)*comb(over_4, 2, exact=True)
  ans += over_14*max(over_4-1, 0)
  ans += over_24*max(over_2-1, 0)
  ans += over_74
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
