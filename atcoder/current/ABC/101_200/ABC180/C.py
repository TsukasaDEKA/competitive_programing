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
        input = """6"""
        output = """1
2
3
6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """720"""
        output = """1
2
3
4
5
6
8
9
10
12
15
16
18
20
24
30
36
40
45
48
60
72
80
90
120
144
180
240
360
720"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000007"""
        output = """1
1000000007"""
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

from itertools import product
import functools
import operator

def resolve():

  N = int(input())
  prime_factors = factorization(N)
  
  answers = set()
  # answer.add(1)

  multiplier_list = []
  for pf in prime_factors:
    multiplier_list.append(list(range(pf[1]+1)))

  # print(list(product(*multiplier_list)))

  list_product = list(product(*multiplier_list))

  for product_ in list_product:
    ans = 1
    for pf, multiplier in zip(prime_factors, product_):
      ans *= pf[0]**multiplier
    answers.add(ans)
  # for pf in prime_factors:

  for a in sorted(list(answers)):
    print(a)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
