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
        input = """RRLRL"""
        output = """0 1 2 1 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """RRLLLLRLRRLL"""
        output = """0 3 3 0 0 0 1 1 0 2 2 0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """RRRLLRLLRRRLLLLL"""
        output = """0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0"""
        self.assertIO(input, output)

def resolve():
  S = list(input())

  # 連続した R と連続した L のペア (例: RRRLLLL) を見つける。(R 開始 L 終わりが保証されているので、必ず全ての R の塊と L の塊はペアになる。)
  # 連続した R と連続した L の長さをそれぞれ R_count、 L_countとすると、
  # R の右端の子供の人数は、L_count//2 + (R_count+1)//2、L の左端の子供の人数は、(L_count+1)//2 + R_count//2 になる。 
  # それ以外のマスの子供の人数は 0 になる。
  N=len(S)
  ans = [0]*N
  i=0
  while True:
    R_count = 0
    while S[i]=="R":
      i+=1
      R_count+=1
    R_index = i-1
    L_index = i

    L_count=0
    while S[i]=="L":
      i+=1
      L_count+=1
      if i>=N: break
    ans[R_index] = L_count//2 + (R_count+1)//2
    ans[L_index] = (L_count+1)//2 + R_count//2
    if i>=N: break
  print(*ans)

resolve()

if __name__ == "__main__":
    unittest.main()
