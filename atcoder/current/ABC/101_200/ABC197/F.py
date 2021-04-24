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
        input = """8 8
1 2 a
2 3 b
1 3 c
3 4 b
4 5 a
5 6 c
6 7 b
7 8 a"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 5
1 1 a
1 2 a
2 3 a
3 4 b
4 4 a"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 4
1 1 a
1 2 a
2 3 b
3 3 b"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [list(map(int, input().split(" "))) for _ in range(N)]
  

  print()

# resolve()

if __name__ == "__main__":
    unittest.main()
