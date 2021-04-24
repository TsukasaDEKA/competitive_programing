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

    def test_入力例1(self):
        input = """7 6
4
3
1
1
2
10
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6 10
10
10
10
10
0
10"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6 9
10
10
10
10
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4 0
1
2
3
4"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 0 がありえるからダメっぽい
  # 要素に 0 が含まれる場合だけ別に考える。
  N, K = map(int, input().split(" "))
  S = [int(input()) for _ in range(N)]
  current = 0
  compressed = [0]*N
  j = 0
  for i in range(N):
    if S[i] == 0:
      print(N)
      return
    if S[i] == 1:
      if compressed[j] <= 0:
        compressed[j] -= 1
      else:
        j+=1
        compressed[j] -= 1
    else:
      if compressed[j] == 0:
        compressed[j] = S[i]
      else:
        j+=1
        compressed[j] = S[i]
      j+=1

  ans = 0
  for l in range(len(compressed)):
    temp_val = 1
    temp_count = 0
    for r in range(l, len(compressed)):
      val = compressed[r]
      if val == 0: break
      if val < 0:
        if temp_val > K: break 
        temp_count -= val
      else:
        if temp_val*val > K: break
        temp_val *= val
        temp_count += 1
    ans = max(ans, temp_count)
  print(ans)
# resolve()

if __name__ == "__main__":
    unittest.main()
