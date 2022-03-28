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
        input = """2 3
2 4
3 2
8 1 5
2 10 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
1 1
2 2
100 1
100 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1
10
100
100
10"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 1
10
100
10
100"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
  import sqlite3

  con = sqlite3.connect(':memory:', isolation_level=None)
  cur = con.cursor()
  cur.executescript("""
  PRAGMA trusted_schema = OFF;
  PRAGMA journal_mode = OFF;
  PRAGMA synchronous = OFF;
  PRAGMA temp_store = memory;
  PRAGMA secure_delete = OFF;
  
  CREATE TABLE boxes(d INT);
  CREATE INDEX boxes_index ON boxes(d);
  """)

  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  chocolates = sorted([(a, b) for a, b in zip(A, B)], reverse=True)

  C = [int(x) for x in input().split(" ")]
  D = [int(x) for x in input().split(" ")]
  boxes = sorted([(c, d) for c, d in zip(C, D)])

  for a, b in chocolates:
    temp = []
    while boxes:
      c, d = boxes[-1]
      if c < a: break
      _, d = boxes.pop()
      temp.append((d, ))
    if temp:
      cur.execute("begin")
      cur.executemany("INSERT INTO boxes(d) VALUES (?)",  temp)
      cur.execute("commit")
    cur.execute("SELECT MIN(d) FROM boxes WHERE d >= ?", (b, ))
    val = cur.fetchone()[0]
    if val is None:
      print("No")
      return
    cur.execute('DELETE FROM boxes WHERE d = ? LIMIT 1', (val, ))
    # cur.execute('DELETE FROM boxes WHERE d = ?', (val, ))
  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()