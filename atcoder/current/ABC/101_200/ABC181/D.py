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
        input = """1234"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1333"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """161"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  S = [int(x) for x in list(input())]

  if len(S) == 1:
    if S[0] == 8:
      print("Yes")
    else:
      print("No")
    return True


  # その数が何個あるかのマップ
  S_map = [0] * 10
  for s in S: S_map[s] += 1


  # 2桁以上の場合
  for i in range(2, 126):
    multiple_of_eight = 8*i

    if multiple_of_eight < 100 and len(S) >= 3: continue

    # 含まれる各数字の個数
    target_map = [0] * 10
    # 文字列に
    str_multiple_of_eight = str(multiple_of_eight)

    for str_num in str_multiple_of_eight:
      target_map[int(str_num)] += 1

    if target_map[0] != 0: continue

    can_create = True
    for i in range(10):
      if S_map[i] < target_map[i]:
        can_create = False
        break

    if can_create:
      print("Yes")
      return True

  print("No")

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
