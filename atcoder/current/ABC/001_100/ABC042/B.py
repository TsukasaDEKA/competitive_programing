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
        input = """3 3
dxx
axx
cxx"""
        output = """axxcxxdxx"""
        self.assertIO(input, output)

def resolve():
  # 辞書順に並び替えて結合する？
  # 文字数が一定なので多分大丈夫
  N, L = map(int, input().split(" "))
  S = sorted([input() for _ in range(N)])

  print(*S, sep="")

resolve()

if __name__ == "__main__":
    unittest.main()
