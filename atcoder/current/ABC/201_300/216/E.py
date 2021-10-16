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
        input = """3 5
100 50 102"""
        output = """502"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2021
2 3"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  target = set()
  target.add(0)

  counter = defaultdict(int)
  for a in A:
    counter[a]+=1
    target.add(a)
  target = sorted(list(target), reverse=True)

  ans = 0
  current_range = 0
  for i in range(len(target)-1):
    current_range += counter[target[i]]
    diff = target[i] - target[i+1]
    a = target[i]
    n = min(diff, K//current_range)

    if diff*current_range >= K:
      # 全部取れるパターン
      # 綺麗に階段畳に取れる
      val = ((n*(2*a-(n-1)))//2)*current_range+(K%current_range)*(a-n)
      ans += val
      break
    else:
      # 全部取れないパターン
      val = ((n*(2*a-(n-1)))//2)*current_range
      ans+=val
      K -= n*current_range
    if K <= 0:
      break
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()