
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
        input = """3 4
1 1
2 2
3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 500000
1 100000
1 100000
1 100000
1 100000
1 100000
100000 100000
100000 100000
100000 100000
100000 100000
100000 100000"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
  # 小さい順にソートして、K 番目の数字ができるまでシミュレートしていく。
  N, K = map(int, input().split(" "))
  A_B = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])

  for a, b in A_B:
    K -= b
    if K<=0:
      print(a)
      return
resolve()

if __name__ == "__main__":
    unittest.main()