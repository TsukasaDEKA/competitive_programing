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

    def test_入力例1(self):
        input = """AABCCD
ABEDDA
EDDAAA"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """AAAAAB
CCCCCB
AAABCB"""
        output = """NO"""
        self.assertIO(input, output)

def resolve():
  # 並べ替えが可能なので Counter を使う。
  # 両方から丁度 N 個文字を取らなきゃいけない。
  # 文字が 26 種類までしかない。
  # S1 からしか取れない文字、
  # S2 からしか取れない文字、
  # 両方から取れる文字、
  # 両方から取れない文字がある。
  # 両方から取りきれないもじが合った時点で NO を返す。

  from collections import Counter
  from collections import defaultdict
  S = [input() for _ in range(3)]
  N = len(S[0])//2

  S1 = defaultdict(int)
  S2 = defaultdict(int)
  S3 = defaultdict(int)
  for i in range(len(S[0])):
    S1[S[0][i]]+=1
    S2[S[1][i]]+=1
    S3[S[2][i]]+=1

  s1_count = 0
  s1_max = 0
  s1_min = 0
  s2_count = 0
  s2_max = 0
  s2_min = 0

  for key, val in S3.items():
    if S1[key] + S2[key] < val:
      print("NO")
      return
    s1_max += min(S1[key], val)
    s1_min += max(0, val-S2[key])
    s2_max += min(S2[key], val)
    s2_min += max(0, val-S1[key])

  if s1_min > N or s2_min > N or s1_max < N or s2_max < N:
     print("NO")
     return
  
  print("YES")

resolve()

if __name__ == "__main__":
    unittest.main()
