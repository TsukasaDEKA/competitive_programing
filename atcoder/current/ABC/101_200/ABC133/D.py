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
2 2 4"""
        output = """4 0 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 8 7 5 5"""
        output = """2 4 12 2 8"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1000000000 1000000000 0"""
        output = """0 2000000000 0"""
        self.assertIO(input, output)

def resolve():
  # 偶数奇数に分けて累積和を取って、
  # 奇数番の山だったらそれより大きい奇数番のダムの水量-それより小さい奇数番のダムの水量-それより大きい偶数番のダムの水量+それより小さい偶数番のダムの水量
  # 偶数番の山だったらそれより大きい偶数番のダムの水量-それより小さい偶数番のダムの水量-それより大きい奇数番のダムの水量+それより小さい奇数番のダムの水量
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  odd_dam  = [0]*(N+1)
  even_dam = [0]*(N+1)
  for i in range(N):
    if (i+1)%2:
      odd_dam[i+1]=A[i]+odd_dam[i]
      even_dam[i+1]=even_dam[i]
    else:
      odd_dam[i+1]=odd_dam[i]
      even_dam[i+1]=A[i]+even_dam[i]
  
  ans = [0]*N
  for i in range(N):
    if (i+1)%2:
      ans[i] = odd_dam[-1] - 2*odd_dam[i] - even_dam[-1] + 2*even_dam[i]
    else:
      ans[i] = even_dam[-1] - 2*even_dam[i] - odd_dam[-1] + 2*odd_dam[i]
  print(*ans)

resolve()

if __name__ == "__main__":
    unittest.main()
