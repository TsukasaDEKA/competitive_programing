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

    def test_入力例_1(self):
        input = """abc"""
        output = """bbb"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """zzzzzzzzzzzzzzzzzzzz"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcdef"""
        output = """fedcba"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """k"""
        output = """bbbbba"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """aa"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """z"""
        output = """aa"""
        self.assertIO(input, output)

def resolve():
  alpha2num = lambda c: ord(c) - ord('a') + 1
  num2alpha = lambda c: chr(c+96)
  inf = 10**18+1
  from collections import Counter
  S = input()
  if S == "zzzzzzzzzzzzzzzzzzzz" or S == "a":
    print("NO")
    return

  countS = Counter(S)
  items = list(countS.items())
  if len(items) == 1:
    # z だけのパターン
    if items[0][0] == "z":
      print(S[:-1]+"ya")
      return
    # 1文字パターン
    if items[0][1] == 1:
      print(num2alpha(alpha2num(items[0][0])-1)+"a")
      return

  hash_bal = 0
  for key, val in items:
    hash_bal += alpha2num(key)*val
  
  ans = "z"*(hash_bal//26)
  sub = num2alpha(hash_bal%26) if hash_bal%26 != 0 else ""
  if S[0] == "z":
    print(sub + ans)
  else:
    print(ans + sub)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
