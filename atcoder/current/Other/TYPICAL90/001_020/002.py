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

    def test_入力例_1(self):
        input = """2"""
        output = """()"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4"""
        output = """(())
()()"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10"""
        output = """((((()))))
(((()())))
(((())()))
(((()))())
(((())))()
((()(())))
((()()()))
((()())())
((()()))()
((())(()))
((())()())
((())())()
((()))(())
((()))()()
(()((())))
(()(()()))
(()(())())
(()(()))()
(()()(()))
(()()()())
(()()())()
(()())(())
(()())()()
(())((()))
(())(()())
(())(())()
(())()(())
(())()()()
()(((())))
()((()()))
()((())())
()((()))()
()(()(()))
()(()()())
()(()())()
()(())(())
()(())()()
()()((()))
()()(()())
()()(())()
()()()(())
()()()()()"""
        self.assertIO(input, output)

def resolve():
  # bit 全探索する。
  # 判定はスタックを使う。
  # 辞書順であることを忘れてた。
  from collections import deque
  inf = 10**18+1
  N = int(input())

  if N%2: return

  ans = []
  for tar in range(pow(2, N)):
    check = 0
    for i in range(N):
      if tar>>i&1:
        check-=1
      else:
        check+=1
      if check < 0:
        break
    if check == 0:
      ans.append("".join(["(" if tar>>i&1 == 0 else ")" for i in range(N)]))
  ans.sort()
  [print(a) for a in ans]

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
