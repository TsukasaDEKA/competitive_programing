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
        input = """1210"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """777"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """123456789"""
        output = """No"""
        self.assertIO(input, output)
def resolve():
  from collections import Counter
  inf = 10**18+1
  S = list(input())
  c = Counter(S)
  if len(c.items()) == 1:
    print("Yes")
    return

  l = 0
  while S[l] == "0":
    l+=1

  r = len(S)-1
  while S[r] == "0":
    r-=1
  
  while l <= r:
    if S[l] != S[r]:
      print("No")
      return
    l+=1
    r-=1
  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
