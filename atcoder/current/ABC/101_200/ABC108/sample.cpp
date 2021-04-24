#include <iostream>
#include <iomanip>
#include <vector>
#include <utility>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <numeric>
#include <set>
#include <complex>
 
using namespace std;
 
struct aaa{aaa(){cin.tie(nullptr); ios::sync_with_stdio(false); cout<<fixed<<setprecision(20);};}aaa;
template <class T>ostream &operator<<(ostream &o,const vector<T>&v){o<<"{";for(int i=0;i<(int)v.size();i++)o<<(i>0?", ":"")<<v[i];o<<"}";return o;}
#define debug(v) {cerr<<"\033[1;36m[debug]\033[m "<<#v<<" : "<<(v)<<endl;}
 
using int64 = long long;
using TP = tuple<int, int, int>;
 
int64 _pow(int n, int k) {
    int res = 1;
    while(k!=0) {
        if (k&1) res *= n;
        n *= n;
        k >>= 1;
    }
    return res;
}
 
int main() {
    int l;
    cin >> l;
 
    int r = 0;
    int _2 = 1;
    while(_2 <= l) r++,_2*=2;
    _2 /= 2;
 
    vector<TP> ans;
 
    int n = r;
    for (int i=1; i<n; i++) {
        ans.emplace_back(i, i+1, 0);
        ans.emplace_back(i, i+1, _pow(2, i-1));
    };
 
 
    for (int i=n; i>=1; i--) {
        if (l - _pow(2, n-1)  <= _pow(2, i-1) - 1) continue;
        l -= _pow(2, i-1);
        ans.emplace_back(i, n, l);
    }
 
 
    cout << n << " " << ans.size() << endl;
    for (const auto& [v, u, c] : ans) {
        cout << v << " " << u << " " << c << endl;
    }
}