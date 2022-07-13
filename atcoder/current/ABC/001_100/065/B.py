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
        input = """3
3
1
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 巡回してるかどうかを見る。
  N = int(input())
  A = [int(input())-1 for _ in range(N)]
  checked = [False]*N
  ans = 0
  current = 0
  while True:
    if current == 1:
      print(ans)
      return
    if checked[current]:
      print(-1)
      return
    checked[current] = True
    current = A[current]
    ans+=1
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()