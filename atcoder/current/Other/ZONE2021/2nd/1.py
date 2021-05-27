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
        input = """2 3 2 5 6 6 7 4 6 2 4 4 14 8 1 9 15 17 5 19
2 2 2 7 7 1 8 6 15 11 4 15 17 26 9 7 21 4 13 10
4 3 2 1 16 4 8 15 26 9 19 11 31 29 9 38 24 27 21 34
3 6 12 8 1 4 23 6 7 26 38 47 36 19 45 28 40 33 9 19
3 5 1 15 5 3 10 20 6 19 15 33 19 27 41 12 66 59 33 35
7 10 10 13 30 2 42 3 55 54 4 51 67 39 59 10 30 2 25 73
4 6 14 16 2 5 48 53 45 62 32 19 26 18 95 63 112 99 112 48
6 5 10 10 11 26 24 55 64 30 65 87 57 60 110 28 127 17 50 78
7 2 12 1 40 22 5 27 58 16 31 15 92 63 128 5 95 159 100 161
6 16 23 28 13 14 5 30 40 70 95 6 32 58 109 138 31 131 110 106
2 18 12 42 40 35 72 48 33 12 112 63 122 9 118 115 187 17 164 34
2 20 32 20 58 56 65 95 80 112 123 24 100 110 1 125 29 70 150 211
7 17 30 10 63 69 43 41 5 84 47 124 21 60 109 65 37 97 57 258
5 20 36 30 64 62 95 112 84 93 6 68 8 106 138 69 197 133 133 106
14 16 7 53 28 47 52 55 7 38 143 17 62 104 61 199 235 124 166 280
16 3 36 51 16 38 45 46 9 24 75 87 94 127 73 50 229 38 132 234
4 12 27 25 46 61 118 55 145 80 157 129 158 218 106 185 286 64 45 147
5 30 13 12 24 25 52 84 157 131 78 177 89 158 96 121 293 306 324 188
9 2 7 8 52 78 107 148 49 105 192 104 116 252 202 96 227 258 211 367
12 10 41 48 4 87 107 102 28 143 24 99 8 234 171 34 72 320 33 295"""
        output = """30"""
        self.assertIO(input, output)

def resolve():
  N = 1000
  prime_numbers = [True]*(N+1)
  prime_numbers[0] = prime_numbers[1] = False
  to = int(-(-N**0.5//1))
  for i in range(2, to+1):
    if not prime_numbers[i]: continue
    target = 2*i
    while target <= N:
      prime_numbers[target] = False
      target+=i

  A = [[int(x) for x in input().split(" ")] for _ in range(20)]

  ans = 0
  for i in range(20):
    for j in range(20):
      if prime_numbers[A[i][j]]: ans+=1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()