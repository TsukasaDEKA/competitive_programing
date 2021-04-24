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
        input = """12 18"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """420 660"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 2019"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7 14"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  A, B = map(int, input().split(" "))

  if min(A,B)==1:
    print(1)
    return
  # A と B の共通の素数の個数を求める。
  # 1 は必ず条件を満たすので count は 1 から
  count = 1

  n = min(A, B)
  for i in range(2, int(-(-n**0.5//1))+1):
    if A%i==0 and B%i==0:
      count += 1

    if A%i==0:
      while A%i==0:
        A //= i

    if B%i==0:
      while B%i==0:
        B //= i

  # 片方が素数でかつ公約数に含まれる場合に +1
  if min(A,B)!=1 and max(A, B)%min(A, B)==0:
    count+=1
  print(count)

# resolve()

if __name__ == "__main__":
    unittest.main()
