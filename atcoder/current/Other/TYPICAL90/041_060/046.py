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
        input = """3
10 13 93
5 27 35
55 28 52"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
10 56 102
16 62 108
20 66 112"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
238 395 46 238 264 114 354 52 324 14 472 64 307 280 209 24 165 194 179 248
270 83 377 332 173 21 362 75 66 342 229 117 124 481 48 235 376 13 420 74
175 427 76 278 486 169 311 47 348 225 41 482 355 356 263 95 170 156 340 289"""
        output = """183"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  # 46 の余りを取って全探索
  N = int(input())
  A = [int(x)%46 for x in input().split(" ")]
  B = [int(x)%46 for x in input().split(" ")]
  C = [int(x)%46 for x in input().split(" ")]
  sumA = [0]*46
  sumB = [0]*46
  sumC = [0]*46
  for i in range(N):
    sumA[A[i]]+=1
    sumB[B[i]]+=1
    sumC[C[i]]+=1

  ans = 0
  for a in range(46):
    if sumA[a] == 0: continue
    for b in range(46):
      if sumB[b] == 0: continue
      for c in range(46):
        if sumC[c] == 0: continue
        if (a+b+c)%46==0: 
          ans += sumA[a]*sumB[b]*sumC[c]

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
