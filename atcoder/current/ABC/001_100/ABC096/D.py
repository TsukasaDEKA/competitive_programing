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
        input = """5"""
        output = """3 5 7 11 31"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6"""
        output = """2 3 5 7 11 13"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8"""
        output = """2 5 7 13 19 37 67 79"""
        self.assertIO(input, output)

def resolve():
  # 55,555 までの素数の中から、 5 で割った余りが全部同じやつの集合であれば、
  # 5*余り + (5 の倍数*5) = 5 の合成数になる。
  N = int(input())
  def get_primes(n):
    prime = ([False, True] * (n//2+1))[0: n+1]
    prime[1] = False
    prime[2] = True
    for i in range(3, int(-(-n**0.5//1))+1, 2):
      if not prime[i]: continue
      for t in range(i*i, n+1, i): prime[t] = False
    return prime

  limit = 55555
  print(*[i for i, is_prime in enumerate(get_primes(limit)) if is_prime and i%5==1][:N], sep=" ")
resolve()

if __name__ == "__main__":
    unittest.main()
