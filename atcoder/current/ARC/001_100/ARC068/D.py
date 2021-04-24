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
        input = """5
1 2 1 3 7"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """15
1 3 5 2 1 3 2 8 8 6 2 6 11 1 1"""
        output = """7"""
        self.assertIO(input, output)

from collections import Counter
def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  numbers_collection = Counter(A)
  # 減らす必要がある枚数を数える。
  has_to_eat = 0
  for _, numbers in numbers_collection.items():
    has_to_eat+=numbers-1
  # 奇数だったら +1 枚追加する。(2 枚づつ減るので)
  if has_to_eat%2: has_to_eat+=1
  print(N-has_to_eat)

resolve()

if __name__ == "__main__":
    unittest.main()
