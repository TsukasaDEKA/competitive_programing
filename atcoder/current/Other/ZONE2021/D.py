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
        input = """ozRnonnoe"""
        output = """zone"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """hellospaceRhellospace"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  inf = 10**18+1
  S = list(input())
  rev = False
  T = deque()

  for i in range(len(S)):
    if S[i] == "R":
      rev = not rev
      continue

    if rev:
      if len(T):
        temp = T.popleft()
        if temp == S[i]: continue
        T.appendleft(temp)
      T.appendleft(S[i])
    else:
      if len(T):
        temp = T.pop()
        if temp == S[i]: continue
        T.append(temp)
      T.append(S[i])

  if len(T):
    if rev:
      T = list(reversed(T))
      print(*T, sep="")
    else:
      print(*T, sep="")
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
