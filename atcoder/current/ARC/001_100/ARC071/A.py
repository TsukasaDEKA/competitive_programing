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
cbaa
daacc
acacac"""
        output = """aac"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
a
aa
b"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  from collections import Counter, defaultdict
  from functools import reduce
  # LCS?
  # 並べ替えが可能なので LCS だと無理っぽい。
  # 全ての Si の要素をカウントして、min を取る。
  # counter を使うと楽に実装できそう。 O(N+S+26*N) (26 はアルファベット分) で間に合う。
  inf = 10**10+1
  N = int(input())
  S = [list(input()) for _ in range(N)]

  common_S = reduce(lambda x, y: set(x) & set(y), S, S[0])

  ans_dict = defaultdict(lambda: inf)

  for S_i in S:
    collection = Counter(S_i)
    for s in common_S:
      ans_dict[s] = min(ans_dict[s], collection[s])

  ans = ""
  for s in sorted(list(common_S)):
    ans+=s*ans_dict[s]
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
