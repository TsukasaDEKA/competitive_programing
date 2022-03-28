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
        input = """3 4
0 0 1
0 1 1 0"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
0
1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5
0 0 1 0 0
0 1 1 0 0"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 5
0 0 1 0 0
1 1 1 1 1"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  S = [int(x) for x in input().split(" ")]
  T = [int(x) for x in input().split(" ")]

  for t in set(T):
    if t not in set(S):
      print(-1)
      return

  if len(set(S)) == 1:
    print(M)
    return

  current = S[0]
  i = 0
  while S[i] == current: i+=1
  len_r = i

  i = N-1
  while S[i] == current: i-=1
  len_l = N-i

  length = min(len_l, len_r)

  ans = 0
  for i in range(M):
    if T[i] == current: ans+=1
    else:
      ans+=length+1
      length = 1
    current = T[i]
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()