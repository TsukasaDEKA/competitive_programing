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
        input = """5
180 186 189 191 218"""
        output = """Yes
1 1
2 3 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
123 523"""
        output = """Yes
1 1
1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
2013 1012 2765 2021 508 6971"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  # 順番は関係ない。
  # 全部の組み合わせについて考える。
  # mod 200 で考える。
  # 余り X を２個以上作れるかどうかの問題。
  # 同じ数字が 2 個あればそれで終わり。
  # 必ず偶数になる。

  N = int(input())
  A = [int(x)%200 for x in input().split(" ")]

  N = min(N, 8)
  agg = [set() for _ in range(200)]
  for i in range(1, 1<<N):
    temp = 0
    for j in range(N):
      if i>>j&1:
        temp+=A[j]
      if temp>=200: temp%=200
    agg[temp].add(i)
    if len(agg[temp]) == 2:
      B, C = list(agg[temp])
      B = [i+1 for i in range(N) if B>>i&1]
      C = [i+1 for i in range(N) if C>>i&1]
      print("Yes")
      print(len(B), *B, sep=" ")
      print(len(C), *C, sep=" ")
      return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
