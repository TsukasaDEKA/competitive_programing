from os import sep
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3"""
        output = """2
1 3
2 3"""
        self.assertIO(input, output)

def resolve():
  # 頂点 N につながる点が必ず存在するので、S は N 以上にならなきゃいけないことがわかる。
  # 頂点を合計値が等しいグループに分けて、同一グループでは連結せず、別のグループ間では連結するケースを考える。
  # 頂点を合計値が等しいグループに分けることができれば、上記の操作で条件を満たせる。
  # 頂点を合計値が等しいグループに分けることができるかを考える。
  # N が偶数の場合 S = N+1 にして、N と 1, N-1 と 2, N-3 と 3・・・　とグループにしていけば良さそう。
  # N が奇数の場合は S = N にして、N, N-1 と 1 ・・・　とグループにしていけば良さそう。
  # グループを環状に繋げればいいので、一つのグループが繋がる別グループは 2 個だけで良さそう。
  inf = 10**18+1
  N = int(input())
  groups = []
  if N%2:
    groups.append([N])
    N-=1
  groups += [[i+1, N-i] for i in range(N//2)]

  ans = set()
  for i in range(len(groups)):
    for f in groups[i]:
      for t in groups[i-1]:
        ans.add((min(f, t), max(f, t)))

  print(len(ans))
  for a in ans:
    print(*a)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()