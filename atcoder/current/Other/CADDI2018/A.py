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
        input = """3 24"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 111"""
        output = """111"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4 972439611840"""
        output = """206"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """1 972439611840"""
        output = """972439611840"""
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
  # 答えを x だとすると、P は x**N で割り切れる。
  # x を探索していけばいい。x**N > P になったらおしまい。
  # 上の方針だと TLE とか出たので方針を変えてみる。
  # P を素因数分解して、それぞれの要素からそれぞれ N 個ずつ取ってみる。
  # 素因数分解に O(sqrt(P)) なので最悪 10**6 程度
  N, P = map(int, input().split(" "))

  fact_P = factorization(P)

  ans = 1
  for fact, count in fact_P:
    if count//N:
      ans*=fact**(count//N)
  print(ans)
resolve()


if __name__ == "__main__":
    unittest.main()
