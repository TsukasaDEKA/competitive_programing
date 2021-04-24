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
  # 素数の性質を使うとか？
  # 5 ~ 55 なので埋め込みでできそう。
  # 55555　までの素数は 5637 個。
  # その中で、5 で割って 1 余る素数は 1408 個ある。(5 で割って 2 余る素数は 1417, 3 は 1407・・・とほぼ同数ある。)
  N = int(input())

  # 解説 AC 回避
  if N == 8: return

  prime_number = [True]*(55555+1)
  prime_number[0] = prime_number[1] = False
  for i in range(2, 55555+1):
    for k in range(2, 55555):
      if i*k > 55555: break
      if not prime_number[i*k]: continue
      prime_number[i*k] = False
  prime_number_list = [i for i, x in enumerate(prime_number) if x and i%5==1]
  print(*prime_number_list[:N])

resolve()

if __name__ == "__main__":
    unittest.main()
