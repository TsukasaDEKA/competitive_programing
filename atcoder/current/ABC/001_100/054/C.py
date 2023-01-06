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
        input = """3 3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # 一筆書き問題だけど、開始点が 1 
  # N が 8 個・・・？二重辺が存在しないので、頂点だけを考えて良い (道を切断しながら動いても良い)
  # 1 が固定で、7! == 5040 パターンあり、一回あたりの計算が 7 かかるので、35000 程度の計算量になるため、
  # 全探索でもいけそう。
  from itertools import permutations
  N, M = map(int, input().split(" "))
  ROUTES = [set() for _ in range(N)]

  for _ in range(M):
    a, b = [int(x)-1 for x in input().split(" ")]
    ROUTES[a].add(b)
    ROUTES[b].add(a)

  patterns = permutations(list(range(1, N)), N-1)
  ans = 0
  for pattern in patterns:
    current = 0
    is_correct = True
    for next_node in pattern:
      if current not in ROUTES[next_node]:
        is_correct = False
        break
      current = next_node
    if is_correct: ans+=1

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
