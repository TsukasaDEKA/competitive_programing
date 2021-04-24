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
#         input = """100
# 1"""
#         output = """19"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """25
# 2"""
#         output = """14"""
#         self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314159
2"""
        output = """937"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
3"""
        output = """117879300"""
        self.assertIO(input, output)



def resolve():
  from scipy.special import comb
  # K が少ない (<= 3) なので、それを利用する。
  N = input()
  K = int(input())

  lenN = len(str(N))
  listN = [int(x) for x in N]
  # 桁 DP とやらを試してみる。
  dp = [[0]*K for _ in range(lenN)]
  dp[0][0] = dp0[0][1] = 1
    
  for i in range(1, lenN):
    for j in range(K):
      

# resolve()

if __name__ == "__main__":
    unittest.main()
