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
3 1
1
2
1
2 3
1 2 1
2 1 2
3 3
3 1 1
3 3 3
2 3 3"""
        output = """Case #1: 4
Case #2: 12
Case #3: 20"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  T = int(input())

  for t in range(1, T+1):
    # キューで管理する？
    # 減る予定があるものを後から取り付けたい。
    E, W = map(int, input().split(" "))
    X = [[int(x) for x in input().split(" ")] for _ in range(E)]

    ans = 0
    que = deque()
    current_weight_count = [0]*W
    for e in range(E):
      # 最初に外す動作を行う。
      for w in range(W):
        while current_weight_count[w] > X[e][w]:
          ans+=1
          removed_w = que.pop()
          current_weight_count[removed_w]-=1

      for l in range(E-e):
        # 追加するとき、最初に「今後の最小値」を決めてから優先的に置くようにする。
        min_weights = [x for x in X[e]]
        for e_ in range(e, E-l):
          for w in range(W):
            min_weights[w] = min(min_weights[w], X[e_][w])

        # ここから先の最小値がわかったので一旦埋める。
        tar_w = sorted([(min_weights[w] - current_weight_count[w], w) for w in range(W)])
        print(l, tar_w, ans)
        for _, w in tar_w:
          while current_weight_count[w] < min_weights[w]:
            ans+=1
            que.append(w)

            current_weight_count[w]+=1
        print(que, current_weight_count)
    ans += len(que)
    print("Case #{0}: {1}".format(t, ans))

# resolve()

if __name__ == "__main__":
  unittest.main()