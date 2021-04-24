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
        input = """1 10
3 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 10
3 5
2 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 1000000000
1 1
1 10000000
1 30000000
1 99999999"""
        output = """860000004"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 500
35 44
28 83
46 62
31 79
40 43"""
        output = """9"""
        self.assertIO(input, output)

from heapq import heapify, heappop, heappush

def resolve():
  N, H = map(int, input().split(" "))
  max_a = 0
  B = []
  heapify(B)
  for i in range(N):
    a, b = [int(x) for x in input().split(" ")]
    max_a = max(a, max_a)
    heappush(B, -1*b)
  
  ans = 0
  while B:
    b = (-1)*heappop(B)
    if b < max_a: break
    ans+=1
    H-=b
    if H<=0:
      print(ans)
      return

  ans += H//max_a
  if H%max_a!=0: ans+=1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
