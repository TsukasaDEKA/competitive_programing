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
        input = """4 10
1 3 5
2 4 4
3 10 6
2 4 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 10
1 3 5
2 4 4
3 10 6
2 3 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 1000000000
0 200000 999999999
2 20 1
20 200 1
200 2000 1
2000 20000 1
20000 200000 1"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
  N, W = map(int, input().split(" "))
  schedules = [[int(x) for x in input().split(" ")] for _ in range(N)]

  time_max = 2*(10**5)+1
  p_in_out = [0]*time_max

  for s, t, p in schedules:
    p_in_out[s] += p
    p_in_out[t] -= p
  
  integra_p = [0]*(time_max+1)
  for i in range(N):
    integra_p[i+1] = integra_p[i]+p_in_out[i]
    if integra_p[i+1] > W:
      print("No")
      return
  print("Yes")

resolve()

if __name__ == "__main__":
    unittest.main()
