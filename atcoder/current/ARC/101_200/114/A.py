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
        input = """2
4 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
47"""
        output = """47"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
3 4 6 7 8 9 10"""
        output = """42"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
8"""
        output = """2"""
        self.assertIO(input, output)




def resolve():
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

  inf = 10**18+1
  N = int(input())
  X = set([int(x) for x in input().split(" ")])

  facts = set()
  for x in X:
    temp = 1
    for f, _ in factorization(x):
      temp*=f
    facts.add(temp)
  
  primes = []
  for f in facts:
    val = []
    for key, _ in factorization(f):
      val.append(key)
    primes.append(val)
  prod = product(*primes)
  ans = inf
  for p in prod:
    p = set(p)
    temp = 1
    for val in p:
      temp*=val
    ans=min(ans, temp)
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
