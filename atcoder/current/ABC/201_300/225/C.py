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

#     def test_Sample_Input_1(self):
#         input = """2 3
# 1 2 3
# 8 9 10"""
#         output = """Yes"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """2 1
# 1
# 2"""
#         output = """No"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """10 4
# 1346 1347 1348 1349
# 1353 1354 1355 1356
# 1360 1361 1362 1363
# 1367 1368 1369 1370
# 1374 1375 1376 1377
# 1381 1382 1383 1384
# 1388 1389 1390 1391
# 1395 1396 1397 1398
# 1402 1403 1404 1405
# 1409 1410 1411 1412"""
#         output = """Yes"""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 6
3 4 5 6 7 8"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  B = [[int(x) for x in input().split(" ")] for _ in range(N)]
  start = B[0][0]

  for i in range(M-1):
    if B[0][i]%7==0:
      print("No")
      return

  if start%7+len(B[0])-1 > 7:
    print("No")
    return

  for n in range(N):
    for m in range(M):
      if B[n][m] != start+n*7+m:
        print("No")
        return

  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()