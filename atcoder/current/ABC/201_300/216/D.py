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
        input = """2 2
2
1 2
2
1 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
2
1 2
2
2 1"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  from collections import deque, defaultdict
  inf = 10**18+1
  # 逆順に考える。
  # 一旦全てのボールを底から取り出す。
  # ペアになった色を一旦全て削除する。
  # 削除したボールを取ってきた筒から新しくボールを取り出す。
  # これを繰り返して削除できなくなったら No
  # 最後まで削除できたら Yes
  N, M = map(int, input().split(" "))

  TUBES = []
  for i in range(M):
    _ = int(input())
    TUBES.append([int(x) for x in input().split(" ")])

  # この上にボールを乗せる。
  deleted_case_id = []
  manage_tube_id = defaultdict(int)
  nexts = deque()
  for i in range(M):
    nexts.append((TUBES[i].pop(), i))

  field = set()
  count = 0
  while nexts:
    color, index = nexts.pop()
    if color in field:
      count+=1
      field.remove(color)
      i = manage_tube_id[color]
      if TUBES[i]:
        # 元々フィールドにあったやつの筒から取り出す。
        nexts.append((TUBES[i].pop(), i))
      if TUBES[index]:
        # 新しく取り出したやつ
        nexts.append((TUBES[index].pop(), index))
    else:
      manage_tube_id[color] = index
      field.add(color)

  print("Yes" if count >= N else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()