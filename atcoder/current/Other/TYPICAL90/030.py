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
        input = """15 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """30 2"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """200 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """869120 1"""
        output = """869119"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """10000000 3"""
        output = """6798027"""
        self.assertIO(input, output)

def resolve():
  # K が物凄く小さい。
  # 素因数 を小さい順に 8 個掛けてみる。
  # 2*3*5*7*11*13*17*19 = 9699690 がほぼ 10**7
  # N が 10**7 だけど、高速素因数分解手法を使えば間に合うかも。
  # 入力例 5 で min_prime_factor の構築に 400ms くらい使ってるけど大丈夫か？
  # 素数の組み合わせで計算して行った方が良さそうな気もする。
  # 高速素因数分解手法だとダメだったので、別の方法を考える。
  # 素数を撒いていく？
  # K == 1 の時、答えは明らかに N-1
  inf = 10**18+1
  mod = 10**9+7
  min_val = [0, 2, 6, 30, 210, 2310, 30030, 510510, 9699690]
  N, K = map(int, input().split(" "))

  if K == 1:
    print(N-1)
    return

  # min_prime_factor[i] : i に含まれる最小の素数
  is_prime = [True]*(N+1)
  prime_count = [0]*(N+1)
  # min_prime_factor = list(range(N+1))
  # min_prime_factor[0] = min_prime_factor[1] = 1
  for i in range(2, N+1):
    if is_prime[i]:
      prime_count[i]+=1
      for j in range(2*i, N+1, i):
        is_prime[j] = False
        prime_count[j]+=1
  
  print(len([i for i, x in enumerate(prime_count) if x >= K]))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
