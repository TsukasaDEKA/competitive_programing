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

    def test_入力例1(self):
        input = """@codeformula why is this contest so easy"""
        output = """codeformula"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """myon @@c @a @aba@a @@bb bbb @@@@@ @a test  @ space  aaa test @a@a  test@takoyaki"""
        output = """a
aba
bb
c
takoyaki"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """no atmark"""
        output = """"""
        self.assertIO(input, output)

def resolve():
  import re
  inf = 10**18+1
  S = input().split("@")
  S[0] = ""
  to_ = set()

  # print(S)
  for s in S:
    if len(s) == 0: continue
    if not s[0].isalpha(): continue
    to_.add(re.split("[\W ]", s)[0])
  to_ = sorted(list(to_))
  print(*to_, sep="\n")
resolve()

if __name__ == "__main__":
    unittest.main()
