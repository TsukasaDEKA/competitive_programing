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
        input = """205894618879050"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """314159265358979"""
        output = """-1"""
        self.assertIO(input, output)



def resolve():
  N = int(input())
  total = 0
  temp = 0
  while N > 1:
    total+=1
    if N%3==0:
      N//=3
    elif N%3==1:
      N//=3
      if temp!=0:
        print(-1)
        return
      temp = total
    else:
      print(-1)
      return

  if total != 30:
    print(-1)
    return
  print(total-temp+1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()