import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """4
dcab"""
        output = """acdb"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
ab"""
        output = """ab"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """16
cabaaabbbabcbaba"""
        output = """aaaaaaabbbbcbbbc"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """17
snwfpfwipeusiwkzo"""
        output = """effwpnwipsusiwkzo"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """10
cccccababa"""
        output = """aaacccbcbc"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """4
acbb"""
        output = """a"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  N = int(input())
  S = list(input())
  agg = defaultdict(list)
  for i in range(N):
    agg[S[i]].append(i)
  
  keys = sorted(list(agg.keys()))
  i = 0
  rev_i = N

  for k in keys:
    while agg[k]:
      # 後ろから見ていく。
      j = agg[k].pop()
      if j >= rev_i: continue
      if j < i: break
      # print(i, S[i], j, S[j], S[i] >= k)
      while S[i] <= S[j]:
        i+=1
        if i >= j:
          # print("hoge", i, j, file=sys.stderr)
          break
      else:
        # 見つかった場合
        S[i], S[j] = S[j], S[i]
        i+=1
        rev_i = j
      if i >= rev_i:
        break

    if i >= rev_i:
      break
      # print("".join(S), file=sys.stderr)

  print("".join(S))


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()