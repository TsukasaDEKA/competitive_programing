import imp
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
        input = """4 3 1
1 2 3 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 2 1
1 3 2 4 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 1 1
1 1 1 1 1"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 8 1
2 7 1 8 2 8 1 8 2 8"""
        output = """36"""
        self.assertIO(input, output)

class SegTree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size
        self.d[p]=x
        for i in range(1,self.log+1):
            self.update(p>>i)
    def get(self,p):
        assert 0<=p and p<self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
          if (l&1):
            sml=self.op(sml,self.d[l])
            l+=1
          if (r&1):
            smr=self.op(self.d[r-1],smr)
            r-=1
          l>>=1
          r>>=1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def max_right(self,l,f):
        assert 0<=l and l<=self.n
        assert f(self.e)
        if l==self.n:
            return self.n
        l+=self.size
        sm=self.e
        while(1):
            while(l%2==0):
                l>>=1
            if not(f(self.op(sm,self.d[l]))):
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l])):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:
                break
        return self.n
    def min_left(self,r,f):
        assert 0<=r and r<self.n
        assert f(self.e)
        if r==0:
            return 0
        r+=self.size
        sm=self.e
        while(1):
            r-=1
            while(r>1 & (r%2)):
                r>>=1
            if not(f(self.op(self.d[r],sm))):
                while(r<self.size):
                    r=(2*r+1)
                    if f(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r& -r)==r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


def resolve():
  # まず、X より大きく、 Y より小さい値で数列を分割する。
  # 次にその数列上で L を固定して二分探索すればよさそう。
  inf = 10**18+1
  N, X, Y = map(int, input().split(" "))
  A = [0]+[int(x) for x in input().split(" ")]+[X+1]
  max_seg = SegTree(A, max, -float('inf'))
  min_seg = SegTree(A, min, float('inf'))

  break_line = []
  for i in range(N+2):
    if A[i] > X or A[i] < Y:
      break_line.append(i)

  def lt_x(x):
    return x < X
  def gt_y(y):
    return y > Y

  ans = 0
  B = len(break_line)
  for i in range(B-1):
    L = break_line[i]+1
    R = break_line[i+1]

    for l in range(L, R):
      r = max(max_seg.max_right(l, lt_x), min_seg.max_right(l, gt_y))
      if r >= R: continue
      ans += R-r

  print(ans)
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()