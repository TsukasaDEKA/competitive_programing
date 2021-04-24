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
        input = """9
3 4 5 5
100000
90000 90000 100000 100000
0"""
        output = """108
706236486"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  for i in range(30):
    N = int(input())
    if N == 0: break
    # 等差数列の和 
    x1, y1, x2, y2 = map(int, input().split(" "))
    ans = 0
    for y in range(y1, y2+1):
      n = x2 - x1 + 1
      a = x1*y
      l = x2*y
      ans += n*(a+l)//2
      if ans > mod: ans%=mod
    print(ans)

resolve()

if __name__ == "__main__":
  unittest.main()