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
        input = """3 10
3
2
1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 100
1
1
1
1"""
        output = """200"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 1000
1
2
3
4
5
6
7
8
9
10"""
        output = """8000"""
        self.assertIO(input, output)

def resolve():
  # 塗り替えの最小枚数を求める。
  from collections import Counter

  N, C = map(int, input().split(" "))
  A = [int(input()) for _ in range(N)]
  odd_count = sorted(Counter(A[0::2]).items(), key=lambda x: x[1], reverse=True)
  odd_count.append((99, 0))
  even_count = sorted(Counter(A[1::2]).items(), key=lambda x: x[1], reverse=True)
  even_count.append((99, 0))
  ans = N
  # 塗り替えない色を選ぶ
  if odd_count[0][0] != even_count[0][0]:
    ans -= odd_count[0][1] + even_count[0][1]
  else:
    ans -= max(odd_count[0][1] + even_count[1][1], odd_count[1][1] + even_count[0][1])
  print(ans*C)

resolve()

if __name__ == "__main__":
    unittest.main()
