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
0
1
1
1
0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
1
1
0
1
1
1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3
1
1
1"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  # 全部同じ色だった場合、終わりがない。
  # 赤と黒の塊だけ見れば良さそう。(境界部分の木は色が変化しないため。)
  # 例 2 の場合、5 本連続しているので、変化させる対象が、3 -> 1 と変化する。
  # 6 本なら 4 -> 2、7 本なら 5 -> 3 -> 1、8 本なら 6 -> 4 -> 2
  # (<連続した木の本数>+1)//2 日後に変化しなくなる。
  # 最大値が答え。
  from collections import Counter
  N = int(input())
  C = [input() for _ in range(N)]
  count = Counter(C)
  if "0" not in count or "1" not in count:
    print(-1)
    return

  tree_groups = []
  tar = C[0]
  count = 1
  for i in range(1, N):
    if C[i] == tar: count+=1
    else:
      tree_groups.append(count)
      count = 1
      tar = C[i]
  
  if C[0] == C[-1]: tree_groups[0] += count
  else: tree_groups.append(count)

  ans = 1
  for t in tree_groups:
    ans = max(ans, (t+1)//2 if t >= 3 else 0)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
