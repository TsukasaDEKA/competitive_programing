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
  rooms = [None] * N

  def search_and_mark(recent_rooms, AB, depth):
    if None not in rooms:
      return rooms

    tmp_rooms = []
    for r in recent_rooms:
      tmp = AB[np.any(AB == r, axis=1)]
      target = tmp[tmp != r]
      tmp_rooms.extend(target)
      AB = AB[np.all(AB != r, axis=1)]
      
      for t in target:
        if rooms[t] == None:
          rooms[t] = r

    recent_rooms = list(set(tmp_rooms))
    return search_and_mark(recent_rooms, AB, depth+1)

  AB = []
  for m in range(M):
    AB.append([int(x) - 1 for x in input().split(" ")])

  AB = np.array(AB)
  result = search_and_mark([0], AB, 0)

  print("Yes")
  for r in result[1:]:
    print(r + 1)

# if __name__ == "__main__":
#     resolve()

if __name__ == "__main__":
    unittest.main()