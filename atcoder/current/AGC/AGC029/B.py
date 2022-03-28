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
        input = """3
1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 11 14 5 13"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  # Ai + Aj が 2 の階乗である時、 Ai + Aj + 2**t も 2 の階乗
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  agg = defaultdict(int)

  for a in A: agg[a]+=1

  keys = list(agg.keys())
  keys.sort(reverse=True)
  ans = 0
  for key in keys:
    v = 2
    while v <= key:
      v*=2
    if v-key == key:
      ans += agg[key]//2
      agg[key] -= agg[key]//2
    else:
      ans += min(agg[v-key], agg[key])
      agg[v-key] -= min(agg[v-key], agg[key])

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()