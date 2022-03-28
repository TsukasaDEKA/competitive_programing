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
        input = """ozRnonnoe"""
        output = """zone"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """hellospaceRhellospace"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  S = list(input())
  N = len(S)

  que = deque()
  turned = False
  for i in range(N):
    if S[i] == "R":
      turned = ~turned
      continue

    if que:
      if turned:
        if que[0] == S[i]: _ = que.popleft()
        else: que.appendleft(S[i])
      else:
        if que[-1] == S[i]: _ = que.pop()
        else: que.append(S[i])
    else:
      que.append(S[i])

  ans = list(que)[::-1] if turned else list(que)
  print("".join(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()