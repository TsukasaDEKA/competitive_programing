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
#         input = """4
# 2 1
# -2 6
# 2 1
# -10 10
# 1 1
# 0
# 3 1
# 2 -2 2"""
#         output = """Case #1: 3
# Case #2: IMPOSSIBLE
# Case #3: -1000000000000000000
# Case #4: 2"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
3 10
-2 3 6
6 2
-2 2 1 -2 4 -1
1 12
-5"""
        output = """Case #1: 0
Case #2: -1 15
Case #3: 1 1 1 1 1 1 1 1 1 1 1"""
        self.assertIO(input, output)

def resolve():
  T = int(input())

  for t in range(1, T+1):
    N, K = map(int, input().split(" "))
    A = [int(x) for x in input().split(" ")]
    sum_A = sum(A)
    integA = 0
    for i in range(N-1):
      for j in range(i+1, N):
        integA += A[i]*A[j]

    # 既に squary であるならば 0 を足せば良い。
    if integA == 0:
      print("Case #{0}: {1}".format(t, 0))
      continue

    # 現状 squary じゃない場合。
    # sum_A が 0 かつ K == 1 なら squary にできない。
    if K == 1:
      if sum_A != 0:
        if integA%sum_A != 0:
          print("Case #{0}: {1}".format(t, "IMPOSSIBLE"))
        else:
          ans = -(integA//sum_A)
          print("Case #{0}: {1}".format(t, ans))
      else:
        print("Case #{0}: {1}".format(t, "IMPOSSIBLE"))
      continue
    
    # K == 1 以上の場合。
    # sum_A == 0 の場合は 1  -integA を足せばいい。
    if sum_A == 0:
      print("Case #{0}: 1 {1}".format(t, -integA))
      continue

    # integA が割り切れる場合は 1 手で終わる。
    if integA%sum_A == 0:
      ans = -(integA//sum_A)
      print("Case #{0}: {1}".format(t, ans))
      continue
    
    # integA が sum_A で割り切れない場合。
    ans = []
    for _ in range(K):
      if integA%sum_A:
        ans.append(-1)
        integA += -sum_A
        sum_A += -1
      else:
        ans.append(-(integA//sum_A))
        print("Case #{0}: {1}".format(t, " ".join([str(x) for x in ans])))
        break
    else:
      print("Case #{0}: {1}".format(t, "IMPOSSIBLE"))

resolve()

if __name__ == "__main__":
  unittest.main()