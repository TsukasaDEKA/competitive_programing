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
        input = """3
011"""
        output = """2
1
1"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """23
# 00110111001011011001110"""
#         output = """2
# 1
# 2
# 2
# 1
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 2
# 1
# 3"""
#         self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
00000000"""
        output = """1
1
1
1
1
1
1
1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """20
11111111111111111111"""
        output = """2
2
2
3
2
2
1
3
3
3
2
3
2
4
3
2
3
2
2
2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1
0"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  X = input()

  if X == "1":
    print(1)
    return True

  if X == "0":
    print(0)
    return 0

  base_1_count = X.count("1")
  X_int = int(X, 2)
  X_int_p = X_int%(base_1_count + 1)
  X_int_m = 1

  if base_1_count > 1:
    X_int_m = X_int%(base_1_count - 1)

# 低速バージョン
  for i in range(N):
    if X[i] == "1":
      Xi = X_int - 2**(N-i-1)
    else:
      Xi = X_int + 2**(N-i-1)
    count = 0
    while Xi != 0:
      # print(Xi)
      num_of_1 = bin(Xi).count("1")
      Xi %= num_of_1
      count += 1
    # print("~~~~~~~~~~~~~~~")
    print(count)

# if __name__ == "__main__":
#     resolve()

if __name__ == "__main__":
    unittest.main()
