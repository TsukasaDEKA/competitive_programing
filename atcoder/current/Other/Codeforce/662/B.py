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
        input = """6
1 1 1 2 1 1
6
+ 2
+ 1
- 1
+ 2
- 1
+ 2"""
        output = """NO
YES
NO
NO
NO
YES"""
        self.assertIO(input, output)

import collections

def resolve():
  N = int(input())
  StrageList = [int(x) for x in input().split(" ")]
  collectionsStrage = collections.Counter(StrageList)

  events = int(input())

  two = 0
  four = 0
  six = 0
  eight = 0

  for planks in collectionsStrage:
    if collectionsStrage[planks] == 2 or collectionsStrage[planks] == 3:
      two += 1
    elif collectionsStrage[planks] == 4 or collectionsStrage[planks] == 5:
      four += 1
    elif collectionsStrage[planks] == 6 or collectionsStrage[planks] == 7:
      six += 1
    elif collectionsStrage[planks] >= 8:
      eight += 1

  for _ in range(events):
    inout = input().split(" ")
    if inout[0] == "+":
      collectionsStrage[int(inout[1])] += 1
      if collectionsStrage[int(inout[1])] == 2:
        two += 1
      elif collectionsStrage[int(inout[1])] == 4:
        two -= 1
        four += 1
      elif collectionsStrage[int(inout[1])] == 6:
        four -= 1
        six += 1
      elif collectionsStrage[int(inout[1])] == 8:
        six -= 1
        eight += 1
    else:
      collectionsStrage[int(inout[1])] -= 1
      if collectionsStrage[int(inout[1])] == 1:
        two -= 1
      elif collectionsStrage[int(inout[1])] == 3:
        two += 1
        four -= 1
      elif collectionsStrage[int(inout[1])] == 5:
        four += 1
        six -= 1
      elif collectionsStrage[int(inout[1])] == 7:
        six += 1
        eight -= 1
    # print("{0},{1},{2},{3},".format(two, four, six, eight))
    if (two >= 1 and six >= 1) or (two >= 2 and four >= 1) or (four >= 2):
      print("YES")
    else:
      print("NO")

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
