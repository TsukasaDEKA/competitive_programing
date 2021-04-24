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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)

import re

def resolve():
  S_base = list(input())
  T = list(input())

  if len(T) > len(S_base):
    print("UNRESTORABLE")
    return True

  for i in reversed(range(len(S_base) - len(T) + 1)):
    isMatched = True
    for t in range(len(T)):
      if not (S_base[i + t] == T[t] or S_base[i + t] == "?"):
        isMatched = False
        break
    if isMatched:
      result = "".join(S_base[:i])+"".join(T)+"".join(S_base[i+len(T):])
      print(result.replace("?", "a"))
      return True

  print("UNRESTORABLE")

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
