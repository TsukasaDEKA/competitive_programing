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
        input = """1225"""
        output = """1360"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """99999"""
        output = """111105"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314159265358979323846264338327950288419716939937510"""
        output = """349065850398865915384738153697722542688574377708317"""
        self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"""
    #     output = """349065850398865915384738153697722542688574377708317"""
    #     self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ
  X = [int(x) for x in list(input())]
  sumX = list(reversed(list(accumulate(X))))
  N = len(X)
  ans = [0]*(N+10)
  # print(sumX)
  for i in range(N):
    val = sumX[i]
    index = i
    while val:
      ans[index] += val%10
      if ans[index] >= 10:
        ans[index+1] += 1
        ans[index]%=10
      index+=1
      val//=10

  for i in reversed(range(len(ans))):
    if ans[i] != 0:
      ans = ans[:i+1]
      break
  ans.reverse()
  print(*ans, sep="")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()