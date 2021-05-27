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
        input = """2 2 4"""
        output = """baab"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """30 30 118264581564861424"""
        output = """bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        self.assertIO(input, output)


def resolve():
  # 総数は 2**60 なので、10**18 程度。
  # 全探索は無理。
  # K が全体のどれくらいかで大体の場所を探知できる。
  from itertools import permutations
  from math import gcd
  inf = 10**18+1
  A, B, K = map(int, input().split(" "))
  factorial = [1]*(A+B+1)
  for i in range(1, A+B+1):
    factorial[i] = factorial[i-1]*i

  def all_pattern(A, B):
    return factorial[A+B]//factorial[A]//factorial[B]
  

  ans = [""]*(A+B)
  for i in range(A+B):
    g = gcd(A, A+B)
    tempA = A//g
    tempAB = (A+B)//g
    center = all_pattern(A, B)//tempAB*tempA
    if K <= center:
      ans[i] = "a"
      A-=1
    else:
      K -= center
      ans[i] = "b"
      B-=1
  print("".join(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
