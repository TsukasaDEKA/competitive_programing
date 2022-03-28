import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """5
3 4 1
7 0 0
0 0 7
0 0 0
1000000000000000 1000000000000000 1000000000000000"""
        output = """2
1
0
0
900000000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  T = int(input())
  for i in range(T):
    N2, N3, N4 = [int(x) for x in input().split(" ")]
    ans = 0

    # 021
    temp = min(N3//2, N4)
    ans+=temp
    N3-=2*temp
    N4-=temp

    # 102
    temp = min(N2, N4//2)
    ans+=temp
    N2-=temp
    N4-=2*temp

    # 220
    temp = min(N2//2, N3//2)
    ans+=temp
    N2-=2*temp
    N3-=2*temp

    # 301
    temp = min(N2//3, N4)
    ans+=temp
    N2-=3*temp
    N4-=2*temp

    # 500
    temp = N2//5
    ans+=temp
    print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()