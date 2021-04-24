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
        input = """8
100 130 130 130 115 115 150 150"""
        output = """1685"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
200 180 160 140 120 100"""
        output = """1000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
157 193"""
        output = """1216"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  diff_of_rate = [0]*(N-1)
  diff_of_rate = []
  diff_of_rate.append({"index": 0, "diff": 0, "price": A[0]})
  for i in range(N-1):
    if (diff_of_rate[-1]["diff"] <= 0 and A[i+1] - A[i] <= 0) or (diff_of_rate[-1]["diff"] >= 0 and A[i+1] - A[i] >= 0):
      diff_of_rate[-1]["index"] = i+1
      diff_of_rate[-1]["diff"] += A[i+1] - A[i]
      diff_of_rate[-1]["price"] = A[i+1]
    else:
      diff_of_rate.append({
        "index": i+1,
        "diff": A[i+1] - A[i],
        "price": A[i+1]
      })

  # print(diff_of_rate)

  # 初期ステータス
  money = 1000
  stock = 0
  price = A[0]

  # 初日の購入
  if diff_of_rate[0]["diff"] > 0:
    stock += money//price
    money = money%price
    
  for index, diff in enumerate(diff_of_rate):
    if diff["diff"] < 0 and index < len(diff_of_rate)-1:
      # 購入
      stock += money//diff["price"]
      money = money%diff["price"]
    else:
      #売却
      money += stock*diff["price"]
      stock = 0

  print(money)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()
