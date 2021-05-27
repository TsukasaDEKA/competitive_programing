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
        input = """50 500
12 18
0 23
15 43
10 33
5 18
2 36
25 36
5 44
9 44
15 17
26 43
29 33
32 37
5 23
6 24
21 22
4 32
27 29
1 20
1 34
12 21
20 37
18 38
14 30
0 30
22 37
5 42
21 22
41 44
35 47
12 47
5 43
41 49
22 27
7 27
3 31
18 36
9 37
19 38
7 37
9 23
40 45
15 35
23 31
32 33
15 47
10 24
1 27
32 49
26 39
13 32
3 17
14 39
39 46
4 30
3 18
4 10
30 33
12 25
41 45
5 19
4 38
10 20
27 45
6 9
22 29
12 18
4 20
10 46
33 38
30 33
14 25
19 46
34 49
0 35
35 37
25 29
43 49
24 48
10 22
4 5
45 49
3 29
18 31
2 16
26 41
15 24
12 32
8 13
35 44
21 47
8 14
10 24
28 43
27 41
1 42
32 47
8 47
7 8
23 43
34 46
9 34
12 32
21 28
36 44
17 27
0 19
4 40
22 34
8 40
15 44
1 49
11 23
28 30
31 41
8 28
7 26
28 43
0 45
8 31
16 23
0 19
6 25
27 34
9 39
8 38
11 42
1 18
13 33
35 39
28 43
11 49
5 36
2 4
12 24
32 42
21 36
6 15
16 26
7 33
27 35
15 19
0 23
20 42
34 45
42 43
2 6
20 37
3 9
12 22
11 23
6 41
6 42
14 22
24 45
12 38
3 25
6 11
14 19
2 13
8 11
12 17
11 23
30 45
17 22
1 38
9 31
32 42
7 46
10 21
26 32
26 39
5 16
9 32
18 43
19 29
28 33
12 36
6 10
1 42
22 29
32 37
13 20
1 20
4 36
11 34
5 15
0 33
1 19
1 15
32 37
17 31
21 35
9 26
5 40
10 34
28 43
2 49
10 28
35 40
7 40
11 44
21 28
34 47
31 37
21 35
4 38
27 29
11 40
5 34
4 20
27 49
1 8
5 35
34 39
2 24
3 47
40 43
8 32
18 44
13 42
18 49
11 24
9 11
3 47
37 38
29 44
36 42
12 32
11 24
33 48
2 44
14 41
10 36
0 35
24 27
12 48
2 13
0 4
30 48
29 36
6 31
5 41
7 13
3 11
13 30
11 40
33 39
4 43
2 24
0 20
35 41
29 38
2 32
11 25
4 24
46 47
27 30
9 20
7 21
16 24
12 23
12 31
4 5
41 47
13 46
1 8
10 36
2 31
34 37
31 33
17 48
3 22
4 37
2 46
22 34
17 41
20 47
10 45
12 30
9 45
6 16
7 23
9 39
6 39
3 36
30 43
12 17
23 31
7 14
8 38
26 43
12 26
7 16
39 46
3 41
9 46
39 46
18 30
20 41
40 41
10 48
17 36
16 23
2 43
14 19
25 38
3 47
27 48
13 47
2 39
31 34
26 31
0 47
40 46
14 28
12 49
20 45
2 9
31 39
2 46
20 49
24 37
16 29
1 13
33 40
6 38
9 40
5 32
18 44
22 29
17 21
38 42
17 41
20 40
29 34
3 29
3 36
36 39
1 48
15 32
21 44
3 40
3 4
9 26
6 29
10 37
3 41
17 32
19 48
12 14
36 49
35 44
11 39
2 43
19 39
6 49
29 34
31 45
22 31
0 3
6 16
26 37
28 42
13 24
36 42
0 5
29 38
46 49
22 37
3 43
9 25
42 44
11 30
5 33
36 47
1 23
10 11
43 46
15 33
27 30
4 22
12 20
3 34
4 37
36 49
3 36
31 38
25 37
20 35
16 18
21 23
7 40
20 35
16 20
29 49
28 33
15 43
26 46
2 35
11 44
1 3
16 42
22 25
9 45
3 36
29 34
0 33
47 49
23 35
6 16
18 23
9 39
41 49
22 46
16 45
23 43
6 39
15 35
13 30
28 44
4 27
7 25
0 5
24 27
16 21
8 12
9 38
16 35
9 39
30 32
14 43
34 49
14 42
39 40
4 12
15 37
0 25
10 37
29 40
2 10
1 29
12 14
16 46
9 38
24 29
21 46
2 17
6 42
24 28
17 22
30 46
6 39
5 19
9 24
19 39
20 30
10 43
41 45
16 22
21 25
36 40
12 14
3 24
8 14
8 36
7 18
7 18
27 42
7 11
38 49
26 38
32 38
8 18
7 25
8 19
15 31
0 10
33 45
27 36
24 43
1 20
16 26
2 46
15 30
9 19
28 36
23 41
3 14
0 31
41 45
35 48
23 42
25 37
3 27
27 28
30 42
3 25
13 14
29 39"""
        output = """30"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  E = [set() for _ in range(N)]
  for _ in range(M):
    A, B = [int(x) for x in input().split(" ")]
    E[A].add(B)
    E[B].add(A)

  temp = 0
  ans = set()
  for i in range(N-2):
    for j in range(i+1, N-1):
      for k in range(j, N):
        union = E[i] | E[j] | E[k] | {i, j, k}
        if temp < len(union):
          temp = len(union)
          ans = [i, j, k]
  print(*ans, sep=" ")
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()