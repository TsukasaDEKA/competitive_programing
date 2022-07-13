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
0224"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
123123"""
        output = """17"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """19
3141592653589793238"""
        output = """329"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = [int(x) for x in list(input())]

  indexes = [[] for _ in range(10)]
  for i in range(N):
    indexes[S[i]].append(i)

  ans = 0
  for i in range(1000):
    key = [int(x) for x in list(f'{i:03d}')]
    # S から key を作れるか判定する。
    if len(indexes[key[0]]) == 0: continue
    if len(indexes[key[1]]) == 0: continue
    if len(indexes[key[2]]) == 0: continue
    
    for j in indexes[key[1]]:
      if indexes[key[0]][0] < j and j < indexes[key[2]][-1]:
        ans += 1
        break

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()