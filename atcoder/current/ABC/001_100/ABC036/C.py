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
        input = """5
3
3
1
6
1"""
        output = """1
1
0
2
0"""
        self.assertIO(input, output)

def resolve():
  # set にしてソートして list に戻して index, value 関係を反転させると対応関係が求まるので、
  # 大体 O(3*N) で解ける。
  N = int(input())
  A = [int(input()) for x in range(N)]

  converter = {e: i for i, e in enumerate(sorted(set(A)))}

  print(converter)
  # ans = [0]*N
  # for i in range(N):
  #   ans[i] = converter(A[i])
  # print(*ans, sep="\n")

# resolve()

if __name__ == "__main__":
    unittest.main()
