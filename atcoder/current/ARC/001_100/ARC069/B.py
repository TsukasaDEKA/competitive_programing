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
        input = """6
ooxoox"""
        output = """SSSWWS"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
oox"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
oxooxoxoox"""
        output = """SSWWSSSWWS"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
xxx"""
        output = """SSW"""
        self.assertIO(input, output)


def resolve():
  # 最初の 2 個を暫定的に置き、そこから矛盾しないように動物の種類を決めていって、
  # 末尾と先頭で矛盾が生じないかを確認すれば良い。
  
  N = int(input())
  S = list(input())

  for i in reversed(range(4)):
    isSheep = [None]*N
    for j in range(2):
      isSheep[j] = ((i>>j)&1==0)

    for j in range(2, N):
      if isSheep[j-1]:
        if S[j-1] == "o": isSheep[j] = isSheep[j-2]
        else: isSheep[j] = not isSheep[j-2]
      else:
        if S[j-1] == "o": isSheep[j] = not isSheep[j-2]
        else: isSheep[j] = isSheep[j-2]

    # 末尾に矛盾が無いかチェック
    # print(*["S" if x else "W" for x in isSheep], sep="")
    if isSheep[-1] and not ((S[-1] == "o" and isSheep[-2]==isSheep[0]) or (S[-1] == "x" and isSheep[-2]!=isSheep[0])): continue
    if isSheep[ 0] and not ((S[ 0] == "o" and isSheep[-1]==isSheep[1]) or (S[ 0] == "x" and isSheep[-1]!=isSheep[1])): continue
    if not isSheep[-1] and not ((S[-1] == "o" and isSheep[-2]!=isSheep[0]) or (S[-1] == "x" and isSheep[-2]==isSheep[0])): continue
    if not isSheep[ 0] and not ((S[ 0] == "o" and isSheep[-1]!=isSheep[1]) or (S[ 0] == "x" and isSheep[-1]==isSheep[1])): continue
    print(*["S" if x else "W" for x in isSheep], sep="")
    return
  print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
