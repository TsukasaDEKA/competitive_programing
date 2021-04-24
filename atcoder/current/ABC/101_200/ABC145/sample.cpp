#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
 
using namespace std;
 
const int MOD = 1'000'000'007;
 
long mpow(long n, long k) {
    long res = 1;
    while(k!=0) {
        if (k&1) res *= n;
        n *= n;
        n %= MOD;
        res %= MOD;
        k /= 2;
    }
 
    return res;
}
 
vector<long> fact(200'006);
vector<long> ifact(200'006);
 
void fact_init(const int n) {
    fact[0] = 1;
    for (int i=1; i<=n; i++) fact[i] = (fact[i-1] * i) % MOD;
    ifact[n] = mpow(fact[n], MOD-2);
    for (int i=n; i>=1; i--) ifact[i-1] = (ifact[i] * i) % MOD;
}
 
int nCr(int n, int r) {
    if (n < r) return 0;
    long res = fact[n];
    res *= ifact[r];
    res %= MOD;
    res *= ifact[n-r];
    return res % MOD;
}
 
int main() {
    long n, m, k;
    cin >> n >> m >> k;
    fact_init(n*m);
 
 
    long ans = 0;
    for (int i=0; i<m; i++) {
        long c = i * (m - i) % MOD;
        c *= n;
        c %= MOD;
        c *= n;
        c %= MOD;
        ans += c;
    }
 
 
    for (int i=0; i<n; i++) {
        long c = i * (n-i) % MOD;
        c *= m;
        c %= MOD;
        c *= m;
        c %= MOD;
        ans += c;
    }
 
    ans %= MOD;
    ans *= nCr(n*m-2, k-2);
    ans %= MOD;
    cout << ans << endl;
}