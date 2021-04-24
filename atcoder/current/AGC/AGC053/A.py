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

#     def test_Sample_Input_1(self):
#         input = """3
# <><
# 3 8 6 10"""
#         output = """2
# 1 5 4 7
# 2 3 2 3"""
#         self.assertIO(input, output)

    def test_Sample_Input_1(self):
        input = """3
<><
3 8 6 10"""
        output = """2
2 4 3 5
1 4 3 5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
<
3 4"""
        output = """1
3 4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
<
3 6"""
        output = """3
1 2
1 2
1 2"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 差が分割数より大きいと良い非不整数列にならない。
  # 差の絶対値の最小値 K で Ai を分割して、余りを 1 ずつできるだけ割り振っていく。
  # 差の分布次第で破綻しそうな気がするけど、差の最小値を使って分割しているので、矛盾が発生しない (はず)
  inf = 10**18+1
  N = int(input())
  S = list(input())
  A = [int(x) for x in input().split(" ")]
 
  K = inf
  for i in range(N):
    K = min(K, abs(A[i+1]-A[i]))

  B = [[0]*(N+1) for _ in range(K)]
  for i in range(N+1):
    for k in range(K):
      B[k][i] = A[i]//K
      if A[i]%K > k: B[k][i]+=1
 
  print(K)
  for b in B:
    print(*b, sep=" ")
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
