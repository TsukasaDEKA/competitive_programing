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
300000 200000 300000 500000
300000 200000 500000 300000
300000 500000 300000 200000
1000000 1000000 0 0
0 1000000 1000000 1000000
999999 999999 999999 999999
768763 148041 178147 984173
699508 515362 534729 714381
949704 625054 946212 951187"""
        output = """Case #1: 300000 200000 300000 200000
Case #2: IMPOSSIBLE
Case #3: 400001 100002 100003 399994"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())

  for i in range(1, T+1):
    printers = [[int(x) for x in input().split(" ")] for _ in range(3)]
    ans = [10**6]*4
    for j in range(3):
      for k in range(4):
        ans[k] = min(ans[k], printers[j][k])
    diff = sum(ans) - 10**6
    if diff < 0:
      print("Case #{0}: IMPOSSIBLE".format(i))
      continue
    
    for j in range(4):
      val = min(ans[j], diff)
      diff -= val
      ans[j] -= val
    print("Case #{0}: {1} {2} {3} {4}".format(i, *ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()