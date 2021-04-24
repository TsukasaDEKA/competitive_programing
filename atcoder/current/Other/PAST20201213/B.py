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
aba"""
        output = """ba"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
sptaast"""
        output = """past"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """30
ryfoxchyvfmsewlwpoyvhdjkbvdjsa"""
        output = """rxcfmelwpoyhkbvdjsa"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = list(input())
  T=""
  already = set()

  for i in reversed(range(N)):
    if S[i] in already:
      S[i]=""
    else:
      already.add(S[i])

  for s in S:
    if s =="": continue
    T+=s

  print(T)

resolve()

if __name__ == "__main__":
    unittest.main()
