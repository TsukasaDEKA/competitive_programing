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
        input = """4
1 2
1 3
4 2
2 3"""
        output = """4"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """2
# 111 111
# 111 111"""
#         output = """1"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """12
# 5 2
# 5 6
# 1 2
# 9 7
# 2 7
# 5 5
# 4 2
# 6 7
# 2 2
# 7 8
# 9 7
# 1 8"""
#         output = """8"""
#         self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # DP?
  # 

  N = int(input())
  A_B = sorted([sorted(list(map(int, input().split(" ")))) for _ in range(N)])
  cards = defaultdict(set)
  ans_set = set()
  for a, b in A_B:
    if b in cards[a]:
      # 同じ組み合わせがある場合は選択を確定する。
      ans_set.add(a)
      ans_set.add(b)
      continue
    if a == b:
      ans_set.add(a)
      continue
    if b not in ans_set:
      cards[a].add(b)


# resolve()

if __name__ == "__main__":
    unittest.main()
