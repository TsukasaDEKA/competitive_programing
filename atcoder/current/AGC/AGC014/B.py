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
        input = """4 4
1 2
2 4
1 3
3 4"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
1 2
3 5
5 1
3 4
2 3"""
        output = """NO"""
        self.assertIO(input, output)

def resolve():
  # imos を使って解く。累積和が全て偶数だったら Yes。(嘘解法かも)
  N, M = map(int, input().split(" "))
  imos_base = [0]*(N)
  for _ in range(M):
    a, b = [int(x)-1 for x in input().split(" ")]
    a, b = min(a, b), max(a, b)
    imos_base[a]+=1
    imos_base[b]-=1
  imos = [0]*(N+1)
  for i in range(N):
    imos[i+1] = imos[i]+imos_base[i]
  
  for i in imos:
    if i%2:
      print("NO")
      return
  print("YES")

resolve()

if __name__ == "__main__":
    unittest.main()
