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

    def test_入力例_1(self):
        input = """42"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """48"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """54"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """53"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  def count_fact(n):
    count = 0
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
      if temp%i==0:
        cnt=0
        while temp%i==0:
          cnt+=1
          temp //= i
        count+=cnt
    if temp!=1: count+=1
    return max(1, count)

  # 現在あるすべてのボールを同時に叩くことができるので、
  # できるだけ素因数の個数が平均的になるように分けた方が叩く回数が少なくなる。
  # 例えば、16 => 2, 8 => 2, 2, 4 => 2, 2, 2, 2 と分けるより、
  # 16 => 4, 4 => 2, 2, 2, 2 と分けた方が叩く回数が少なくなる。
  # 最初に素因数分解して、含まれている素因数の個数を何回割れるか計算する。
  # もうちょっと早そうな実装がありそう。
  N = int(input())
  count = count_fact(N)
  ans = 0
  while count > 1:
    ans += 1
    count=(count+1)//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
