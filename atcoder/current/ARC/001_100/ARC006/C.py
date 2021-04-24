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

    def test_入力例_1(self):
        input = """5
4
3
1
2
1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
93
249
150
958
442
391
25"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
100
100
100
100"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
5
10
15
20
25
30"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  # N<=50 なので push していっても間に合いそう
  N = int(input())
  W = [int(input()) for _ in range(N)]
  ans = [W[0]]
  for w in W[1:]:
    if ans[-1] < w:
      ans.append(w)
      continue

    for i in range(len(ans)):
      if ans[i] >= w:
        ans[i] = w
        ans.sort()
        break
      
  print(len(ans))

resolve()

if __name__ == "__main__":
    unittest.main()
