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
        input = """3
1 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
2 4 8 16"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4
2 3 5 7"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  # 全ての要素を 2 で割り切ってから重複が無いように数える。
  # せいぜいそれぞれの要素毎に 30 回程度の操作しかしないので間に合う。
  ans = set()
  for a in A:
    while a%2==0:
      a //= 2
    ans.add(a)
  print(len(ans))

resolve()

if __name__ == "__main__":
    unittest.main()
