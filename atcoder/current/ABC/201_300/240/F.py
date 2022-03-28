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
        input = """3
3 7
-1 2
2 3
-3 2
10 472
-4 12
1 29
2 77
-1 86
0 51
3 81
3 17
-2 31
-4 65
4 23
1 1000000000
4 1000000000"""
        output = """4
53910
2000000002000000000"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  T = int(input())

  for _ in range(T):
    N, M = [int(x) for x in input().split(" ")]
    C = [[int(x) for x in input().split(" ")] for _ in range(N)]
    # B の N 番目の初項、終項、傾き、項数
    B = []
    a, b = 0, 0
    for i in range(N):
      x, y = C[i]
      a = b+x
      b = a+(x*(y-1))
      B.append((a, b, x, y))

    # A の当該区間における最大値
    ans = -inf
    val = 0
    for i in range(N):
      a, b, x, y = B[i]
      ans = max(ans, val+a)
      if b >= 0:
        # b が正の時、最後まで見るのが最適。
        ans = max(ans, val+(y*(a+b))//2)
      elif a <= 0:
        # b が負で、かつ、a も負の時、これ以上良くなることはない
        pass
      else:
        # a が正で b が負の時、B[i] が 0 になる項までを見る。
        l = (a+abs(x)-1)//abs(x)
        ans = max(ans, val + (l*(2*a + (l-1)*x))//2)
      val += y*(a+b)//2

    # print(val, a, b, x, y, ans)
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()