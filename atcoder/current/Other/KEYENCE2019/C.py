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
        input = """3
2 3 5
3 4 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
2 3 3
2 2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
17 7 1
25 6 14"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """12
757232153 372327760 440075441 195848680 354974235 458054863 463477172 740174259 615762794 632963102 529866931 64991604
74164189 98239366 465611891 362739947 147060907 118867039 63189252 78303147 501410831 110823640 122948912 572905212"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  # diff[i] = A[i]-B[i] を作ってソートする。
  # diff のマイナスの項の数と総和をとる。
  # 大きい順に和を取って、マイナスの総和を超えるための項数をとる。
  # マイナスの項の数 + マイナスを埋めるために使った項の数が答え。
  inf = 10**10+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  if sum(A) < sum(B):
    print(-1)
    return

  diff = [0]*N
  ans = 0
  minus_total = 0
  for i in range(N):
    diff[i] = A[i]-B[i]
    if diff[i] < 0:
      ans+=1
      minus_total+=diff[i]
  diff.sort()

  for i in reversed(range(N)):
    if minus_total>=0: break
    minus_total+=diff[i]
    ans+=1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
