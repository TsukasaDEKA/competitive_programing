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
        input = """4 4
1 2
2 3
3 4
4 2"""
        output = """Yes
1
2
2"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6"""
        output = """Yes
6
5
5
1
1"""
        self.assertIO(input, output)

import numpy as np



def resolve():
  N, M = map(int, input().split(" "))
  AB_map = [[] for i in range(N)]
  for m in range(M):
    AB = [int(x) - 1 for x in input().split(" ")]
    AB_map[AB[0]].append(AB[1])
    AB_map[AB[1]].append(AB[0])

  not_finished = set(range(1, N+1))
  rooms = [None] * N
  rooms[0] = 0
  room_depths = [0] * N

  # def search_and_mark(recent_rooms, depth):
  #   if len(not_finished) == 0 or len(recent_rooms) == 0 or depth >= N:
  #     return True

  #   temp_recent = set()
  #   for r in recent_rooms:
  #     for target in AB_map[r]:
  #       if target in not_finished:
  #         temp_recent.add(target)
  #         not_finished.remove(target)
  #         rooms[target] = r
  #         room_depths[target] = depth

  #   return search_and_mark(list(temp_recent), depth+1)

  # _ = search_and_mark([0], 0)

  recent_rooms = [0]
  depth = 1
  while len(not_finished) != 0 and depth < N:
    temp_recent = set()
    for r in recent_rooms:
      for target in AB_map[r]:
        if target in not_finished:
          temp_recent.add(target)
          not_finished.remove(target)
          rooms[target] = r
          room_depths[target] = depth
    depth += 1
    recent_rooms = list(temp_recent)

  print("Yes")
  for r in rooms[1:]:
    print(r + 1)


if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()