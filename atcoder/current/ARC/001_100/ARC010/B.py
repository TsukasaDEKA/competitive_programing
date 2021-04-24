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
        input = """1
1/9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
1/10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1/7"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1/7
1/9"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """2
12/31
12/30"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
  month_to_date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
  N = int(input())
  M_D = [list(map(int, input().split("/"))) for _ in range(N)]

  holidays = [i%7==1 or i%7==0 for i in range(366+1)]
  for M, D in M_D:
    day = D
    for i in range(1, M):
      day += month_to_date[i]
    while holidays[day]:
      day+=1
      if day>=366:
        day = 366
        break
    holidays[day] = True
    del M, D

  ans=0
  count=0
  for i in range(1, 366+1):
    if holidays[i]:
      count+=1
    else: count=0
    ans=max(ans, count)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
