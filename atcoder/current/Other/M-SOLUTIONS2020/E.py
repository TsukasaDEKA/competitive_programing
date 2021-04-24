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
        input = """3
1 2 300
3 3 600
1 4 800"""
        output = """2900
900
0
0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 5 400
5 3 700
5 5 1000
5 7 700
7 5 400"""
        output = """13800
1600
0
0
0
0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
2 5 1000
5 2 1100
5 5 1700
-2 -5 900
-5 -2 600
-5 -5 2200"""
        output = """26700
13900
3200
1200
0
0
0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8
2 2 286017
3 1 262355
2 -2 213815
1 -3 224435
-2 -2 136860
-3 -1 239338
-2 2 217647
-1 3 141903"""
        output = """2576709
1569381
868031
605676
366338
141903
0
0
0"""
        self.assertIO(input, output)


def resolve():
  N = int(input())
  Villages = []

  for _ in range(N):
    Villages.append([int(x) for x in input().split(" ")])
  print(Villages)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()
