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
        input = """4
2 1
2 2
5 1
1 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
2 1
2 1
2 1
2 1
2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
273 691"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())
  A_B = [list(map(int, input().split(" "))) for _ in range(N)]

  A_B = sorted(A_B, key=lambda x: 2*x[0]+x[1], reverse=True)
  aoki = 0
  for a, _ in A_B:
    aoki += a
  
  ans = 0
  takahashi = 0
  for a, b in A_B:
    takahashi+=2*a+b
    ans+=1
    if takahashi > aoki:
      print(ans)
      return

resolve()

if __name__ == "__main__":
    unittest.main()
