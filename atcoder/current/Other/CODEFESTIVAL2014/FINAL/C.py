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
        input = """49"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """999999999999999"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10000000000000000"""
        output = """10000"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  list_N = list(reversed([int(x) for x in str(N)]))

  for K in range(10, 10001):
    list_K = list(reversed([int(x) for x in str(K)]))
    temp = 0
    for i in range(len(list_K)):
      temp += list_K[i]*(K**i)
    if temp == N:
      print(K)
      return
  print(-1)

resolve()

if __name__ == "__main__":
    unittest.main()
