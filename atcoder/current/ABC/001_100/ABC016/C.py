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
        input = """3 2
1 2
2 3"""
        output = """1
0
1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1 2
1 3
2 3"""
        output = """0
0
0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8 12
1 6
1 7
1 8
2 5
2 6
3 5
3 6
4 5
4 8
5 6
5 7
7 8"""
        output = """4
4
4
5
2
3
4
2"""
        self.assertIO(input, output)

def resolve():
  # 友達の友達の友達の・・・は友達に含まれないっぽい。(サンプルより)
  # 最小距離 2 の関係は友達の友達
  # 幅優先探索で距離 2 の対象を数えていけば良さそう。
  # N <= 10なので全探索しても間に合う。
  from collections import defaultdict, deque
  inf = 10**10+1
  N, M = map(int, input().split(" "))
  friends = defaultdict(set)

  for _ in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    friends[A].add(B)
    friends[B].add(A)
  
  ans = [0]*N
  next_ = deque()
  for i in range(N):
    step = [0]*N
    checked = [False]*N
    checked[i] = True
    next_.append(i)
    while next_:
      current = next_.popleft()
      for friend in friends[current]:
        if checked[friend]: continue
        checked[friend] = True
        if step[current] == 1:
          ans[i]+=1
          continue
        step[friend] = step[current] + 1
        next_.append(friend)
  print(*ans, sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
