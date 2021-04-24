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
        input = """20"""
        output = """17"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100000"""
        output = """30555"""
        self.assertIO(input, output)


def resolve():
  inf = 10**10+1
  N = int(input())
  sevens = [True]*N
  seven_octed = 7
  ans = 0
  for i in range(1, N+1):
    temp_i = i
    is_seven = False
    while temp_i > 0:
      if temp_i%8 == 7:
        is_seven=True
        break
      temp_i//=8

    if is_seven: continue

    temp_i = i
    while temp_i > 0:
      if temp_i%10 == 7:
        is_seven=True
        break
      temp_i//=10
    if is_seven: continue
    ans+=1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()

