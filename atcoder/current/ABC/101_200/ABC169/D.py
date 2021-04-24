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
        input = """24"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """64"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1000000007"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """997764507000"""
        output = """7"""
        self.assertIO(input, output)

# https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
# 素因数分解

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
  N = int(input())
  prime_factors = factorization(N)
  # tri_dict = {
  #   1 :  1,
  #   2 :  1,
  #   3 :  2,
  #   4 :  2,
  #   5 :  2,
  #   6 :  3,
  #   7 :  3,
  #   8 :  3,
  #   9 :  3,
  #   10 :  4,
  #   11 :  4,
  #   12 :  4,
  #   13 :  4,
  #   14 :  4,
  #   15 :  5,
  #   16 :  5,
  #   17 :  5,
  #   18 :  5,
  #   19 :  5,
  #   20 :  5,
  #   21 :  6,
  #   22 :  6,
  #   23 :  6,
  #   24 :  6,
  #   25 :  6,
  #   26 :  6,
  #   27 :  6,
  #   28 :  7,
  #   29 :  7,
  #   30 :  7,
  #   31 :  7,
  #   32 :  7,
  #   33 :  7,
  #   34 :  7,
  #   35 :  7,
  #   36 :  8,
  #   37 :  8,
  #   38 :  8,
  #   39 :  8,
  #   40 :  8,
  #   41 :  8,
  #   42 :  8,
  #   43 :  8,
  #   44 :  8,
  #   45 :  9,
  #   46 :  9,
  #   47 :  9,
  #   48 :  9,
  #   49 :  9,
  #   50 :  9,
  #   51 :  9,
  #   52 :  9,
  #   53 :  9,
  #   54 :  9,
  #   55 :  9,
  #   56 :  9,
  #   57 :  9,
  #   58 :  9,
  #   59 :  9
  # }
  result = 0

  for prime_factor in prime_factors:
    if prime_factor[0] == 1:
      continue

    for count in range(2, 42):
      if prime_factor[1] < (count + 1)*count//2:
        result += count - 1
        break
  print(result)

if __name__ == "__main__":
    unittest.main()
