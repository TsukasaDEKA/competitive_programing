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
        input = """3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6"""
        output = """30"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000"""
        output = """972926972"""
        self.assertIO(input, output)

def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp //= i
      arr.append([i, cnt])

  if temp!=1:
    arr.append([temp, 1])

  if arr==[]:
    arr.append([n, 1])

  return arr


def resolve():
  mod = 10**9+7
  N = int(input())
  # 素数の出現数を求めて、それらの組み合わせが何パターンあるか調べる。
  divisors = [{} for x in range(N+1)]
  # 素数の出現数を求める
  num_of_occurrences = [0]*(N+1)

  # メモかとかでもっと高速化できそうだけどとりあえず素因数分解してみる。(N*logN 以下なので多分大丈夫)
  for n in range(2, N+1):
    prime_factors = factorization(n)
    for number, multiplier in prime_factors:
      num_of_occurrences[number] += multiplier

  # 組み合わせのパターン数を求める
  ans=1
  for num in num_of_occurrences[2:]:
    ans*=num+1
    if ans>mod: ans%=mod
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
