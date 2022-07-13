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
        input = """3
3 8
3 18
1 1000"""
        output = """6
10
900"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
12 201"""
        output = """11"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())

  # テストケースは少ない 10**4
  # 「連続した」部分文字列である点に注意する。
  # 包除を使いそう。
  # 例えば 16 をとると 1, 6, 16 が使えなくなる。
  # 1, 6 を取ったほうがお得。
  # 1 を取ると使えなくなる要素がかなり多い。
  # 大きい方から取っていった方がお得？
  for t in range(T):
    l_str, r_str = input().split(" ")
    r = int(r_str)
    l = int(l_str)
    if r <= 9:
      print(r-l+1)
      continue

    r_str = list(r_str)
    if int(r_str[0]) == 1:
      l = max(l, int("".join(r_str[1:]))+1, r//10+1, (10**(len(r_str)-2)))
    else:
      l = max(l, (10**(len(r_str)-1)))
    # print(r, l)
    print(r-l+1)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()