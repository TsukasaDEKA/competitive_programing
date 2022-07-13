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
        input = """1
869
120"""
        output = """749"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
8 6 9 1 2 0
1 5 7 2 3 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
31 41 59 26 53 58 97 93 23 84
17 32 5 8 7 56 88 77 29 35"""
        output = """211"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """20
804289382 846930886 681692776 714636914 957747792 424238335 719885386 649760491 596516649 189641420 25202361 350490026 783368690 102520058 44897761 967513925 365180539 540383425 304089172 303455735
35005211 521595368 294702567 726956428 336465782 861021530 278722862 233665123 145174065 468703135 101513928 801979801 315634021 635723058 369133068 125898166 59961392 89018454 628175011 656478041"""
        output = """2736647674"""
        self.assertIO(input, output)

def resolve():
  _ = int(input())
  print(sum([abs(a-b) for a, b in zip(sorted(map(int, input().split(" "))), sorted(map(int, input().split(" "))))]))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()