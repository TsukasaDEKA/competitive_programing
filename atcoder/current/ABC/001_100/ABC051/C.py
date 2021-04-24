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
        input = """0 0 1 2"""
        output = """UURDDLLUUURRDRDDDLLU"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """-2 -2 1 1"""
        output = """UURRURRDDDLLDLLULUUURRURRDDDLLDL"""
        self.assertIO(input, output)

def resolve():
  sx, sy, tx, ty = [int(x) for x in input().split(" ")]

  ans = ""
  # 1 往復目
  ## 往路上向
  for _ in range(ty-sy): ans += "U"
  ## 往路右向
  for _ in range(tx-sx): ans += "R"
  ## 復路下向
  for _ in range(ty-sy): ans += "D"
  ## 復路左向
  for _ in range(tx-sx): ans += "L"

  # 2 往復目
  ans+="L"
  ## 往路上向
  for _ in range(ty-sy+1): ans += "U"
  ## 往路右向
  for _ in range(tx-sx+1): ans += "R"
  ans+="DR"
  ## 復路下向
  for _ in range(ty-sy+1): ans += "D"
  ## 復路左向
  for _ in range(tx-sx+1): ans += "L"
  ans+="U"

  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
