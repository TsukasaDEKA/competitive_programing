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
        input = """2 3
7 9"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 0
3 4 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202"""
        output = """292638192"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 答えを L とした時に K 回のカットでそれを実現できるかを探索していく？
  # L を二分探索 ( K が足りないなら L を長くして K が余るなら L を短くする ) すれば O(Nlog(maxA))
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  A.sort()
  
  # ここから二分探索
  ans = A[-1]
  left = 1
  right = A[-1]

  while left < right:
    l = (left+right)//2
    tempK = K
    for a in A:
      if a <= l: continue
      tempK-= a//l
      if a%l==0: tempK+=1
      if tempK<0: break
    
    if tempK >= 0:
      ans = min(ans, l)
      if right == l: break
      right = l
    else:
      if left == l: break
      left = l
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
