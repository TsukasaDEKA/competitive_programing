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
        input = """2 6
1 2 4
2 2 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 1000000000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """163089627821228"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 100000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """88206004785464"""
        self.assertIO(input, output)

def resolve():
  # imos でやる (最大値は C 円)
  # defaultdict でやる
  from collections import defaultdict

  N, prime_val = map(int, input().split(" "))
  events = defaultdict(int)
  event_days = set()

  for i in range(N):
    A, B, C = map(int, input().split(" "))
    events[A]+=C
    events[B+1]-=C
    event_days.add(A)
    event_days.add(B+1)

  event_days = sorted(list(event_days))
  current_val = 0
  last_day = 0
  ans = 0
  for day in event_days:
    ans+=min(prime_val, current_val)*(day-last_day)
    last_day = day
    current_val += events[day]
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()
