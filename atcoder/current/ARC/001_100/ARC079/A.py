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
        input = """3 2
1 2
2 3"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 3
1 2
2 3
3 4"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100000 1
1 99999"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 5
1 3
4 5
2 3
2 4
1 4"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

def resolve():
  # 深さ優先探索をして、2 手で N に辿り着けるかどうか判定
  from collections import deque

  N, M = map(int, input().split(" "))
  X = [set() for _ in range(N)]
  for _ in range(M):
    a, b = [int(x)-1 for x in input().split(" ")]
    X[a].add(b)
    X[b].add(a)

  next_ = deque()
  next_.append(0)
  checked = [False]*N
  checked[0] = True
  step = [0]*N
  while next_:
    current = next_.popleft()
    for i in X[current]:
      if checked[i]: continue
      checked[i] = True
      if step[current] == 1 and i == N-1:
        print("POSSIBLE")
        return
      if step[current] >= 2: continue
      step[i] = step[current]+1
      next_.append(i)
  print("IMPOSSIBLE")

resolve()

if __name__ == "__main__":
    unittest.main()
