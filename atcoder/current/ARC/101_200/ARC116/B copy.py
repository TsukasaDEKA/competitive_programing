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
        input = """3
2 4 3"""
        output = """63"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """1
# 10"""
#         output = """100"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """7
# 853983 14095 543053 143209 4324 524361 45154"""
#         output = """206521341"""
#         self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
1 2 3 4 5"""
        output = """243"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  mod = 998244353
  # 全ての部分列なのでソートしても大丈夫
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  ans = 0
  for i in range(1, 2**N):
    min_ = inf
    max_ = 0
    for j in range(N):
      if i&1<<j:
        min_ = min(min_, A[j])
        max_ = max(max_, A[j])
    ans += min_*max_
  print(ans)
# resolve()

if __name__ == "__main__":
    unittest.main()
