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
        input = """kasaka"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """php"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """aaaphpaaaaaa"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """aaaaaa"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  S = list(input())[::-1]
  N = len(S)

  back = 0
  for i in range(N):
    if S[i] != "a":
      S = S[i:][::-1]
      back = i
      break
  
  front = 0
  for i in range(N):
    if S[i] != "a":
      S = S[i:]
      front = i
      break
  
  if back < front:
    print("No")
    return
  # print("".join(S), "".join(S[::-1]))
  print("Yes" if S == S[::-1] else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()