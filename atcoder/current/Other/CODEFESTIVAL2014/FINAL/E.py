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
        input = """4
1 2 5 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6
1 1 3 4 5 4"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
  # 上がる点が連続するまたは下がる点が連続していた場合、間の点を除外するようにする。
  # 残った点が 3 個未満だったら 0 にする。
  N = int(input())
  R = [int(x) for x in input().split(" ")]

  count = 0
  # 最初の 2 点を見て上がったか下がったか確認する。
  if N < 3:
    print(0)
    return
  start_i = 1
  while R[start_i]==R[0]:
    count+=1
    start_i+=1
    if start_i == N:
      print(0)
      return

  is_up = R[start_i] > R[0]
  for i in range(start_i+1, N):
    if (R[i] >= R[i-1] and is_up) or (R[i] <= R[i-1] and not is_up): count+=1
    else: is_up = not is_up
  print(N-count if N-count > 2 else 0)

resolve()


if __name__ == "__main__":
    unittest.main()
