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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)

def resolve():
  # 遺伝子の塩基配列？
  # クエリがめっちゃ多い
  # AC の累積和を出しておけば O(N*Q)
  # クエリが閉区間な点に注意
  inf = 10**10+1
  N, Q = map(int, input().split(" "))
  S = input()
  integral_AC = [0]*(N+1)

  for i in range(1, N):
    integral_AC[i+1]=integral_AC[i]
    if S[i-1:i+1] == "AC": integral_AC[i+1]+=1

  for i in range(Q):
    L, R = map(int, input().split(" "))
    print(integral_AC[R]-integral_AC[L])

resolve()

if __name__ == "__main__":
    unittest.main()
