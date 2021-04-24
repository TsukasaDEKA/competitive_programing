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
2 2 3
3 1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 2
2 2 3
3 3"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3 4
10 10 10
1 1 1 1"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """10 10
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1"""
        output = """YES"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  # 両方ソートしたらいける？
  rooms = sorted([int(x) for x in input().split(" ")])
  gusts = sorted([int(x) for x in input().split(" ")])

  i = 0
  for g in gusts:
    if i >= N:
      print("NO")
      return
    while rooms[i] < g:
      i+=1
      if i >= N:
        print("NO")
        return
    i+=1
  print("YES")

resolve()

if __name__ == "__main__":
    unittest.main()
