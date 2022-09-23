#ifdef INCLUDED_MAIN

// const ll ansmod = 998244353;
// const ll ansmod = 1000000007;

auto solve() {
    GET(N);
    GET2(N, K);
    // A = [[int(x) + i, i - int(x)] for i, x in enumerate(input().split(" "))]
    GETVLL(A);
    // A = [int(input()) for _ in range(N)] vll A; rep(i, N) {GET(a); A.pb(a);} と同等
    GETVVLL(A, N);
    // S = list(input()) GETSTR(S); で文字列取得
    GETVSTR(S_map, H);

    return _0;
}

int main() {
    auto ans = solve();
    // auto ans = (ansmod + (solve() % ansmod)) % ansmod;
    print(ans);
}

// 以下は動作確認未実施
#else
#define INCLUDED_MAIN
#include <algorithm>
#include <bits/extc++.h>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cstddef>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <stack>
#include <string_view>
#include <type_traits>
#include <utility>
using namespace std;
// clang-format off
/* accelration */
// 高速バイナリ生成
#pragma GCC target("avx")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
// cin cout の結びつけ解除, stdioと同期しない(入出力非同期化)
// cとstdの入出力を混在させるとバグるので注意
struct IOSetting {IOSetting() {std::cin.tie(0); ios::sync_with_stdio(false); cout << fixed << setprecision(15);}} iosetting;

/* alias */
using ull = __uint128_t;
// using ll = long long; // __int128でTLEするときに切り替える。
using ll = __int128;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<ll>;
using vd = vector<double>;
using vvi = vector<vi>;
using vvl = vector<vl>;
using vvll = vector<vll>;
using vs = vector<string>;
using vvs = vector<vs>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using umpll = unordered_map<ll, ll>;
using umpsl = unordered_map<string, ll>;
using mpll = map<ll, ll>;
using sll = set<ll>;
using msll = multiset<ll>;
using heapqll = priority_queue<ll, vll, greater<ll>>;
using heapqllrev = priority_queue<ll>;
using dll = deque<ll>;

/* REP macro */
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define repsp(i, a, n, s) for (ll i = (a); i < (ll)(n); i += s)
#define rep(i, n) reps(i, 0, n)
#define rrep(i, n) reps(i, 1, n + 1)
#define repd(i,n) for(ll i=n-1;i>=0;i--)
#define rrepd(i,n) for(ll i=n;i>=1;i--)
#define repdict(key, value, dict) for (const auto& [key, value] : dict)
#define repset(x, st) for(auto x : st)

/* define short */
#define endl "\n"
#define pf emplace_front
#define pb emplace_back
#define popleft pop_front
#define popright pop_back
#define mp make_pair
#define all(obj) (obj).begin(), (obj).end()
#define len(x) (ll)(x.size())
#define MAX(x) *max_element(all(x))
#define MIN(x) *min_element(all(x))
#define SET(x) sll(all(x))
#define VEC(x) vll(all(x))
#define GET(x) ll x = in_ll();
#define GET2(x, y) ll x, y; {vll _A_ = in_lls(); x = _A_[0]; y = _A_[1];}
#define GET3(x, y, z) ll x, y, z; {vll _A_ = in_lls(); x = _A_[0]; y = _A_[1]; z = _A_[2];}
#define GET4(x, y, z, a) ll x, y, z, a; {vll _A_ = in_lls(); x = _A_[0]; y = _A_[1]; z = _A_[2]; a = _A_[3];}
#define GET5(x, y, z, a, b) ll x, y, z, a, b; {vll _A_ = in_lls(); x = _A_[0]; y = _A_[1]; z = _A_[2]; a = _A_[3]; b = _A_[4];}
#define GET6(x, y, z, a, b, c) ll x, y, z, a, b, c; {vll _A_ = in_lls(); x = _A_[0]; y = _A_[1]; z = _A_[2]; a = _A_[3]; b = _A_[4]; c = _A_[5];}
#define GETVLL(x) vll x = in_lls();
#define GETVVLL(x, N) vvll x; rep(i, N) {GETVLL(ab); x.pb(ab);}
#define GETSTR(x) string x = in_str();
#define GETSTRS(x) vs x; x = in_strs();
#define GETVSTR(x, N) vs x; rep(i, N) x.pb(in_str());
#define INI(x, vec) auto x = vec[0];
#define INI2(x, y, vec) auto x = vec[0], y = vec[1];
#define INI3(x, y, z, vec) auto x = vec[0], y = vec[1], z = vec[2];
#define INI4(x, y, z, a, vec) auto x = vec[0], y = vec[1], z = vec[2], a = vec[3];
#define INI5(x, y, z, a, b, vec) auto x = vec[0], y = vec[1], z = vec[2], a = vec[3], b = vec[4];
#define INI6(x, y, z, a, b, c, vec) auto x = vec[0], y = vec[1], z = vec[2], a = vec[3], b = vec[4], c = vec[5];
#define SETPERM(x, N) vll x(N); iota(all(x), 0);
#define SETPERMS(x, s, N) vll x(N); iota(all(x), s);
#define UNUSED(x) ((void)x);
#define printF(x) print(x); cout << flush;
// [INT|LLONG|DBL]_[MAX|MIN] 最大最小表現

// 型変換
#define STRCHAR(x) (""s + x)
#define STRBIN2LL(x) std::stoull(x, nullptr, 2)
#define STRLL(x) parse(x)
#define CHARLL(x) std::stoll(STRCHAR(x))

/* sort */
#define SORT(x) stable_sort(all(x))
#define RSORT(x) stable_sort(all(x), std::greater<ll>())
#define SORT_IDX(x, idx) stable_sort(all(x), [&](const vll &_a_, const vll &_b_){return _a_[idx] < _b_[idx];})
#define RSORT_IDX(x, idx) stable_sort(all(x), [&](const vll &_a_, const vll &_b_){return _a_[idx] > _b_[idx];})
#define LB_IDX_VEC(c, x) distance((c).begin(), lower_bound(all(c), x)) // O(log N)
#define UB_IDX_VEC(c, x) distance((c).begin(), upper_bound(all(c), x)) // O(log N)
#define LB_ITR_VEC(c, x) lower_bound(all(c), x)
#define UB_ITR_VEC(c, x) upper_bound(all(c), x)
#define LB_IDX_SET(c, x) distance((c).begin(), c.lower_bound(x)) // O(N)
#define UB_IDX_SET(c, x) distance((c).begin(), c.upper_bound(x)) // O(N)
#define LB_ITR_SET(c, x) c.lower_bound(x)
#define UB_ITR_SET(c, x) c.upper_bound(x)
#define LB_ITR_MAP(c, x) c.lower_bound(x)
#define UB_ITR_MAP(c, x) c.upper_bound(x)
#define KEY_CHANGE(c, k1, k2) { auto i_ = c.extract(k1); i_.key() = k2; c.insert(std::move(i_));}
#define EXIST(key, dict) (dict.find(key) != dict.end())
#define REV(x) reverse(all(x))

namespace // 直値のデフォルトの型をllに。
{
    ll _0 = 0;
    ll _1 = 1;
    ll _2 = 2;
    ll _3 = 3;
    ll _4 = 4;
    ll _5 = 5;
    ll _6 = 6;
    ll _7 = 7;
    ll _8 = 8;
    ll _9 = 9;
    ll _10 = 10;
    ll _11 = 11;
    ll _12 = 12;
    ll _13 = 13;
    ll _14 = 14;
    ll _15 = 15;
    ll _16 = 16;
    ll _17 = 17;
    ll _30 = 30;
    ll _31 = 31;
    ll _32 = 32;
    ll _33 = 33;
    ll _63 = 63;
    ll _64 = 64;
    ll _65 = 65;
    ll _66 = 66;
    ll _126 = 126;
    ll _127 = 127;
    ll _128 = 128;
    ll _129 = 129;
};

void ignore_warning() // ワーニング対策
{
    _0 = _0;
    _1 = _1;
    _2 = _2;
    _3 = _3;
    _4 = _4;
    _5 = _5;
    _6 = _6;
    _7 = _7;
    _8 = _8;
    _9 = _9;
    _10 = _10;
    _11 = _11;
    _12 = _12;
    _13 = _13;
    _14 = _14;
    _15 = _15;
    _16 = _16;
    _17 = _17;
    _30 = _30;
    _31 = _31;
    _32 = _32;
    _33 = _33;
    _63 = _63;
    _64 = _64;
    _65 = _65;
    _66 = _66;
    _126 = _126;
    _127 = _127;
    _128 = _128;
    _129 = _129;
}

/* helper func */
std::ostream &operator<<(std::ostream &dest, __int128 value) {
  std::ostream::sentry s(dest);
  if (s) {
    __uint128_t tmp = value < 0 ? -value : value;
    char buffer[128];
    char *d = std::end(buffer);
    do {
      --d;
      *d = "0123456789"[tmp % 10];
      tmp /= 10;
    } while (tmp != 0);
    if (value < 0) {
      --d;
      *d = '-';
    }
    int len = std::end(buffer) - d;
    if (dest.rdbuf()->sputn(d, len) != len) {
      dest.setstate(std::ios_base::badbit);
    }
  }
  return dest;
}

ll parse(string &s) {
  ll ret = 0;
  bool isplus = true;
  for (ll i = 0; i < s.length(); i++)
    if ('0' <= s[i] && s[i] <= '9')
      ret = 10 * ret + s[i] - '0';
    else if (s[i] == '-')
      isplus ^= isplus;
  return isplus ? ret : -ret;
}

template <typename T>
string STR(T v) {
    ostringstream ss;
    ss << v;
    return ss.str();
}

ll SUM(const vll &v) {
    ll total = 0;
    rep(i, len(v)) {
        total += v[i];
    }
    return total;
}

ll POPLEFT(dll &q) {
    const ll v = q.front();
    q.pop_front();
    return v;
}

ll POP(dll &q) {
    const ll v = q.back();
    q.pop_back();
    return v;
}

void HEAPPUSH(heapqll &q, ll v) {
    q.push(v);
}

ll HEAPPOP(heapqll &q) {
    const ll v = q.top();
    q.pop();
    return v;
}

void HEAPPUSH(heapqllrev &q, ll v) {
    q.push(v);
}

ll HEAPPOP(heapqllrev &q) {
    const ll v = q.top();
    q.pop();
    return v;
}

template<class... T>
constexpr auto min(T... a){
    return min(initializer_list<common_type_t<T...>>{a...});
}

template<class... T>
constexpr auto max(T... a){
    return max(initializer_list<common_type_t<T...>>{a...});
}

// search_length: 走査するベクトル長の上限(先頭から何要素目までを検索対象とするか、1始まりで)
template <typename T> inline bool vector_finder(std::vector<T> vec, T element, unsigned int search_length) {
    auto itr = std::find(vec.begin(), vec.end(), element);
    size_t index = std::distance( vec.begin(), itr );
    if (index == vec.size() || index >= search_length) {return false;} else {return true;}
}
inline void print(const sll& v, string s = " ")
    {bool first = true; for(auto &p : v) { if(first) {first = false; cout << p;} else cout << s << p;} cout << endl;}
inline void print(const msll& v, string s = " ")
    {bool first = true; for(auto &p : v) { if(first) {first = false; cout << p;} else cout << s << p;} cout << endl;}
template <typename T> inline void print(const vector<T>& v, string s = " ")
    {rep(i, v.size()) cout << v[i] << (i != (ll)v.size() - 1 ? s : "\n");}
inline void print(const vvll& v, string s = " ")
    {rep(i, len(v)) print(v[i], s);}
template <typename T, typename S> inline void print(const pair<T, S>& p)
    {cout << p.first << " " << p.second << endl;}
template <typename T> inline void print(const T& x) {cout << x << endl;}
template <typename T, typename S> inline void print(const vector<pair<T, S>>& v)
    {for (auto&& p : v) print(p);}
template <typename T, typename S> inline void print(const unordered_map<T, S>& d)
    {for (const auto& [key, value] : d) {cout << key << " "; print(value);}}
template <typename T, typename S> inline void print(const map<T, S>& d)
    {for (const auto& [key, value] : d) {cout << key << " "; print(value);}}
// 第一引数と第二引数を比較し、第一引数(a)をより大きい/小さい値に上書き
template <typename T> inline bool chmin(T& a, const T& b) {bool compare = a > b; if (a > b) a = b; return compare;}
template <typename T> inline bool chmax(T& a, const T& b) {bool compare = a < b; if (a < b) a = b; return compare;}

/* func */
inline ll in_ll() {string s; getline(cin, s); return STRLL(s);}
inline string in_str() {string s; getline(cin, s); return s;}

inline string YESNO(bool cond) {return cond ? "YES" : "NO";}
inline string yesno(bool cond) {return cond ? "yes" : "no";}
inline string YesNo(bool cond) {return cond ? "Yes" : "No";}

/* debug */
namespace debug_print_func {
    std::ostream& os = std::cerr;

    template <class Tp> auto has_cbegin(int)     -> decltype(std::cbegin(std::declval<Tp>()), std::true_type {});
    template <class Tp> auto has_cbegin(...)     -> std::false_type;
    template <class Tp> auto has_value_type(int) -> decltype(std::declval<typename Tp::value_type>(), std::true_type {});
    template <class Tp> auto has_value_type(...) -> std::false_type;

    template <class Tp>[[maybe_unused]] constexpr bool is_iteratable_container_v = decltype(has_cbegin<Tp>(int {}))::value;
    template <class Tp>[[maybe_unused]] constexpr bool is_container_v            = decltype(has_value_type<Tp>(int {}))::value
                                                                                    || is_iteratable_container_v<Tp>;

    template <>        [[maybe_unused]] constexpr bool is_iteratable_container_v<std::string_view> = false;
    template <>        [[maybe_unused]] constexpr bool is_container_v<std::string_view>            = false;
    #if (defined _GLIBCXX_STRING) || (defined _LIBCPP_STRING)
    template <>        [[maybe_unused]] constexpr bool is_iteratable_container_v<std::string>      = false;
    template <>        [[maybe_unused]] constexpr bool is_container_v<std::string>                 = false;
    #endif

    template <class Tp, class... Ts> struct first_element { using type = Tp; };
    template <class... Ts> using first_t = typename first_element<Ts...>::type;

    template <class Tp, std::enable_if_t<!decltype(has_value_type<Tp>(int {}))::value, std::nullptr_t> = nullptr>
        auto check_elem(int) -> decltype(*std::cbegin(std::declval<Tp>()));
    template <class Tp, std::enable_if_t<decltype(has_value_type<Tp>(int {}))::value, std::nullptr_t> = nullptr>
        auto check_elem(int) -> typename Tp::value_type;
    template <class Tp>
        auto check_elem(...) -> void;

    template <class Tp> using elem_t = decltype(check_elem<Tp>(int {}));

    template <class Tp> [[maybe_unused]] constexpr bool is_multidim_container_v = is_container_v<Tp>
                                                                                    && is_container_v<elem_t<Tp>>;

    template <class Tp> std::enable_if_t<!is_container_v<Tp>> out(const Tp&);
    void out(const char&);
    void out(const char*);
    void out(const std::string_view&);

    #if (defined _GLIBCXX_STRING) || (defined _LIBCPP_STRING)
    void out(const std::string&);
    #endif

    #ifdef __SIZEOF_INT128__
    void out(const __int128&);
    void out(const unsigned __int128&);
    #endif

    template <class Tp1, class Tp2> void out(const std::pair<Tp1, Tp2>&);

    #if (defined _GLIBCXX_TUPLE) || (defined _LIBCPP_TUPLE)
    template <class... Ts> void out(const std::tuple<Ts...>&);
    #endif

    #if (defined _GLIBCXX_STACK) || (defined _LIBCPP_STACK)
    template <class... Ts> void out(std::stack<Ts...>);
    #endif

    #if (defined _GLIBCXX_QUEUE) || (defined _LIBCPP_QUEUE)
    template <class... Ts> void out(std::queue<Ts...>);
    template <class... Ts> void out(std::priority_queue<Ts...>);
    #endif

    template <class C>
    std::enable_if_t<is_iteratable_container_v<C>> out(const C&);

    template <class Tp> std::enable_if_t<!is_container_v<Tp>> out(const Tp& arg) {
        os << arg;
    }

    void out(const char& arg) {
        os << '\'' << arg << '\'';
    }

    void out(const char* arg) {
        os << '\"' << arg << '\"';
    }

    void out(const std::string_view& arg) {
        os << '\"' << arg << '\"';
    }

    #if (defined _GLIBCXX_STRING) || (defined _LIBCPP_STRING)
    void out(const std::string& arg) {
        os << '\"' << arg << '\"';
    }
    #endif

    #ifdef __SIZEOF_INT128__
    void out(const __int128& arg) {
        int sign = (arg < 0) ? (-1) : 1;
        if (sign == -1)
        os << '-';
        __int128 base = sign;
        while (sign * arg >= sign * base * 10)
        base *= 10;
        while (base) {
        os << static_cast<char>('0' + (arg / base % 10));
        base /= 10;
        }
    }

    void out(const unsigned __int128& arg) {
        unsigned __int128 base = 1;
        while (arg >= base * 10)
        base *= 10;
        while (base) {
        os << static_cast<char>('0' + (arg / base % 10));
        base /= 10;
        }
    }
    #endif

    template <class Tp1, class Tp2> void out(const std::pair<Tp1, Tp2>& arg) {
        os << '(';
        out(arg.first);
        os << ", ";
        out(arg.second);
        os << ')';
    }

    #if (defined _GLIBCXX_TUPLE) || (defined _LIBCPP_TUPLE)
    template <class T, std::size_t... Is> void print_tuple(const T& arg, std::index_sequence<Is...>) {
        static_cast<void>(((os << (Is == 0 ? "" : ", "), out(std::get<Is>(arg))), ...));
    }

    template <class... Ts> void out(const std::tuple<Ts...>& arg) {
        os << '(';
        print_tuple(arg, std::make_index_sequence<sizeof...(Ts)>());
        os << ')';
    }
    #endif

    #if (defined _GLIBCXX_STACK) || (defined _LIBCPP_STACK)
    template <class... Ts> void out(std::stack<Ts...> arg) {
        if (arg.empty()) {
        os << "<empty stack>";
        return;
        }
        os << "[ ";
        while (!arg.empty()) {
        out(arg.top());
        os << ' ';
        arg.pop();
        }
        os << ']';
    }
    #endif

    #if (defined _GLIBCXX_QUEUE) || (defined _LIBCPP_QUEUE)
    template <class... Ts> void out(std::queue<Ts...> arg) {
        if (arg.empty()) {
        os << "<empty queue>";
        return;
        }
        os << "[ ";
        while (!arg.empty()) {
        out(arg.front());
        os << ' ';
        arg.pop();
        }
        os << ']';
    }
    template <class... Ts> void out(std::priority_queue<Ts...> arg) {
        if (arg.empty()) {
        os << "<empty priority_queue>";
        return;
        }
        os << "[ ";
        while (!arg.empty()) {
        out(arg.top());
        os << ' ';
        arg.pop();
        }
        os << ']';
    }
    #endif

    template <class Container>
    std::enable_if_t<is_iteratable_container_v<Container>> out(const Container& arg) {
        if (std::distance(std::cbegin(arg), std::cend(arg)) == 0) {
        os << "<empty container>";
        return;
        }
        os << "[ ";
        std::for_each(std::cbegin(arg), std::cend(arg), [](const elem_t<Container>& elem) {
        out(elem);
        os << ' ';
        });
        os << ']';
    }

    template <class Tp> std::enable_if_t<!is_multidim_container_v<Tp>>
    print(std::string_view name, const Tp& arg) {
        os << name << ": ";
        out(arg);
        if constexpr (is_container_v<Tp>)
        os << '\n';
    }

    template <class Tp> std::enable_if_t<is_multidim_container_v<Tp>>
    print(std::string_view name, const Tp& arg) {
        os << name << ": ";
        if (std::distance(std::cbegin(arg), std::cend(arg)) == 0) {
        os << "<empty multidimensional container>\n";
        return;
        }
        std::for_each(std::cbegin(arg), std::cend(arg),
        [&name, is_first_elem = true](const elem_t<Tp>& elem) mutable {
            if (is_first_elem)
            is_first_elem = false;
            else
            for (std::size_t i = 0; i < name.length() + 2; i++)
                os << ' ';
            out(elem);
            os << '\n';
        });
    }

    template <class Tp, class... Ts> void multi_print(std::string_view names, const Tp& arg, const Ts&... args) {
        if constexpr (sizeof...(Ts) == 0) {
        names.remove_suffix(
            std::distance(
            names.crbegin(),
            std::find_if_not(names.crbegin(), names.crend(),
                            [](const char c) { return std::isspace(c); })
            )
        );
        print(names, arg);
        if constexpr (!is_container_v<Tp>)
            os << '\n';
        } else {
        std::size_t comma_pos = 0;

        for (std::size_t i = 0, paren_depth = 0, inside_quote = false; i < names.length(); i++) {
            if (!inside_quote && paren_depth == 0 && i > 0 && names[i - 1] != '\'' && names[i] == ',') {
            comma_pos = i;
            break;
            }
            if (names[i] == '\"') {
            if (i > 0 && names[i - 1] == '\\') continue;
            inside_quote ^= true;
            }
            if (!inside_quote && names[i] == '(' && (i == 0 || names[i - 1] != '\''))
            paren_depth++;
            if (!inside_quote && names[i] == ')' && (i == 0 || names[i - 1] != '\''))
            paren_depth--;
        }

        const std::size_t first_varname_length = comma_pos - std::distance(
            names.crend() - comma_pos,
            std::find_if_not(
            names.crend() - comma_pos, names.crend(),
            [](const char c) { return std::isspace(c); }
            )
        );
        print(names.substr(0, first_varname_length), arg);

        if constexpr (!is_container_v<Tp>) {
            if constexpr (is_container_v<first_t<Ts...>>)
            os << '\n';
            else
            os << " | ";
        }

        const std::size_t next_varname_begins_at = std::distance(
            names.cbegin(),
            std::find_if_not(
            names.cbegin() + comma_pos + 1, names.cend(),
            [](const char c) { return std::isspace(c); }
            )
        );
        names.remove_prefix(next_varname_begins_at);

        multi_print(names, args...);
        }
    }
}  // namespace debug_print

#ifdef LOCAL
#  define debug(...) cerr << "\033[33m(line:" << __LINE__ << ") " << endl; debug_print_func::multi_print(#__VA_ARGS__, __VA_ARGS__); cerr << "\033[m";
#else
#  define debug(...) ;
#endif

/* 標準入力 */
vs in_strs(const string &delimiter = " ")
{
    string s;
    getline(cin, s);

    vs output;
    bitset<255> delims;
    for (unsigned char c: delimiter)
    {
        delims[c] = true;
    }
    string::const_iterator beg;
    bool in_token = false;
    for( string::const_iterator it = s.cbegin(), end = s.cend(); it != end; ++it )
    {
    if( delims[*it] )
    {
    if( in_token )
    {
        output.pb(beg, it);
        in_token = false;
    }
    }
    else if( !in_token )
    {
        beg = it;
        in_token = true;
    }
    }
    if( in_token )
        output.pb(beg, s.cend());
    return output;
}

inline vll in_lls()
{
    vll vals;
    vs tokens = in_strs();
    for (string i: tokens) vals.pb(STRLL(i));
    return vals;
}

inline vvll in_llss(ll line) // 複数行文字列解析
{
    vvll valss;
    rep(i, line) valss.pb(in_lls());
    return valss;
}

inline vs in_vs(ll line) // 複数行文字列解析
{
    vs vecs;
    rep(i, line) {
        vecs.pb(in_str());
    }
    return vecs;
}

inline ll popcnt(ll x) { return __builtin_popcountll(x); }

template <typename T, typename U>
T ceil(T x, U y) {
  return (x > 0 ? (x + y - 1) / y : x / y);
}

template <typename T, typename U>
T floor(T x, U y) {
  return (x > 0 ? x / y : (x - y + 1) / y);
}

template <typename T, typename U>
pair<T, T> divmod(T x, U y) {
  T q = floor(x, y);
  return {q, x - q * y};
}

inline ll sumk(ll n)
{
    return n * (n + 1) / 2;
}

inline ll sumk2(ll n)
{
    return n * (n + 1) * (2 * n + 1) / 6;
}

ll accxor(ll n)
{
    ll v = (n + 1) % 4;
    if (v == 0)
        return 0;
    else if (v == 1)
        return n;
    else if (v == 2)
        return 1;
    else
        return 1 ^ n;
}

inline string alpha()
{
    return "abcdefghijklmnopqrstuvwxyz";
}

inline ll alpha_num(char c)
{
    return ll(c) - ll('a');
}

inline string alpha_big()
{
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
}

inline ll alpha_big_num(char c)
{
    return ll(c) - ll('A');
}

string zerofill(ll v, ll outputlen)
{
    string s = STR(v);
    string zerostr(outputlen - len(s), '0');
    return zerostr + s;
}

template <class T> vll z_algorithm(const std::vector<T>& s) {
    ll n = (ll)(s.size());
    if (n == 0) return {};
    vll z(n);
    z[0] = 0;
    for (ll i = 1, j = 0; i < n; i++) {
        ll& k = z[i];
        k = (j + z[j] <= i) ? 0 : std::min(j + z[j] - i, z[i - j]);
        while (i + k < n && s[k] == s[i + k]) k++;
        if (j + z[j] < i + z[i]) j = i;
    }
    z[0] = n;
    return z;
}

vll z_algorithm(const std::string& s) {
    ll n = (ll)(s.size());
    vll s2(n);
    for (ll i = 0; i < n; i++) {
        s2[i] = s[i];
    }
    return z_algorithm(s2);
}

string ll2str(ll x, ll base) {
    if(x == 0) return "0";
    stringstream ss;
    string ret;
    auto ll2base = [&]() {
        stringstream tmp;
        string cs = "0123456789" + alpha() + alpha_big();
        while (x > 0) {
            tmp << cs[(x % base)];
            x /= base;
        }
        ret = tmp.str();
        REV(ret);
    };
    switch(base) {
        case 8:
            ss << std::oct << x; ret = ss.str(); break;
        case 10:
            ss << std::dec << x; ret = ss.str(); break;
        case 16:
            ss << std::hex << x; ret = ss.str(); break;
        default:
            ll2base();
            break;
    }
    return ret;
}

inline vvll init_tbl(int h, int w, ll val = 0)
{
    vvll tbl(h, vll(w, val));
    return tbl;
}

constexpr ll safe_mod(ll x, ll m) {
    x %= m;
    if (x < 0) x += m;
    return x;
}

constexpr std::pair<ll, ll> inv_gcd(ll a, ll b) {
    a = safe_mod(a, b);
    if (a == 0) return {b, 0};

    ll s = b, t = a;
    ll m0 = 0, m1 = 1;

    while (t) {
        ll u = s / t;
        s -= t * u;
        m0 -= m1 * u;

        auto tmp = s;
        s = t;
        t = tmp;
        tmp = m0;
        m0 = m1;
        m1 = tmp;
    }
    if (m0 < 0) m0 += b / s;
    return {s, m0};
}

ll inv_mod(ll x, ll m) {
    assert(1 <= m);
    auto z = inv_gcd(x, m);
    assert(z.first == 1);
    return z.second;
}

/*
vll r = {2, 3, 2};
vll m = {3, 5, 7};
INI2(a, b, crt(r, m));
debug(a, b);
としたとき
a: 23 | b: 105
これは、x≡2 (mod 3), x≡3 (mod 5), x≡2 (mod 7)の解が
x = 105k + 23ということを示す
*/
vll crt(const std::vector<ll>& r, const std::vector<ll>& m) {
    assert(r.size() == m.size());
    ll n = ll(r.size());
    // Contracts: 0 <= r0 < m0
    ll r0 = 0, m0 = 1;
    for (ll i = 0; i < n; i++) {
        assert(1 <= m[i]);
        ll r1 = safe_mod(r[i], m[i]), m1 = m[i];
        if (m0 < m1) {
            std::swap(r0, r1);
            std::swap(m0, m1);
        }
        if (m0 % m1 == 0) {
            if (r0 % m1 != r1) return {0, 0};
            continue;
        }

        ll g, im;
        std::tie(g, im) = inv_gcd(m0, m1);

        ll u1 = (m1 / g);
        if ((r1 - r0) % g) return {0, 0};
        ll x = (r1 - r0) / g % u1 * im % u1;

        r0 += x * m0;
        m0 *= u1;
        if (r0 < 0) r0 += m0;
    }
    return vll{r0, m0};
}

// rep(i, n) floor((a * i + B), M)を高速に求める。
ll floor_sum(ll n, ll m, ll a, ll b) {
    ll ans = 0;
    if (a >= m) {
        ans += (n - 1) * n * (a / m) / 2;
        a %= m;
    }
    if (b >= m) {
        ans += n * (b / m);
        b %= m;
    }

    ll y_max = (a * n + b) / m, x_max = (y_max * m - b);
    if (y_max == 0) return ans;
    ans += (n - (x_max + a - 1) / a) * y_max;
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a);
    return ans;
}

ll POW(ll n, ll r)
{
    if (r == 0) return 1;
    else if (r % 2 == 0) return POW(n * n, (ll)(r / 2));
    else return n * POW(n, r - 1);
}


#define mod_m2p(a, m) ((m + a) % m)
#define mod_add(a, b, m) ((a + b) % m)
#define mod_sub(a, b, m) ((m + a - b) % m)
#define mod_mul(a, b, m) (mod_m2p((a % m) * (b % m), m))
ll mod_bipow_(ll x, ll y, ll m) {   // x^y by bisection method
    if (y == 0) return 1 % m;
    else if (y == 1) return x % m;
    else if (y % 2 == 0) {
        ll val = mod_bipow_(x, (ll)(y / 2), m);
        return mod_mul(val, val, m);
    } else {
        ll val = mod_bipow_(x, (ll)(y / 2), m);
        return mod_mul(mod_mul(val, val, m), x, m);
    }
}

ll mod_inv(ll x, ll pm) { return mod_bipow_(mod_m2p(x, pm), pm - 2, pm); }   // x^{-1} = x^{MOD-2} (MOD: prime number)
ll mod_div(ll a, ll b, ll m) { return mod_mul(mod_m2p(a, m), mod_inv(mod_m2p(b, m), m), m); }   // a/b = a*b^{-1}
ll mod_bipow(ll x, ll y, ll m) {
    if (y < 0) {
        ll xx = mod_div((ll)1, x, m);
        return mod_bipow_(xx, -y, m);
    }
    return mod_bipow_(x, y, m);
}

// 尺取りのベース関数
auto syakutori(const vll &vec) {
    ll N = len(vec);
    ll val = 0, cnt = 0;
    ll l = 0, r = 0;
    while (l < N)
    {
        // if (val == N) ++cnt; カウントする条件を記載
        bool cond = N < val; // 判定範囲を超えたかどうか
        if ((r == N) || cond)
        {
            // val -= vec[l]; // 範囲を縮小するときに演算する処理
            ++l;
        }
        else // 範囲を拡大するときに演算する処理
        {
            // val += vec[r];
            ++r;
        }
    }
    return cnt;
}

// 連続した要素の部分和がsvalと等しくなる個数をカウント。O(N)
auto subsum(const vll &vec, const ll sval) {
    ll N = len(vec);
    ll val = 0, cnt = 0;
    ll l = 0, r = 0;
    while (l < N)
    {
        if (val == sval)
            ++cnt;
        if ((r == N) || sval < val)
        {
            val -= vec[l];
            ++l;
        }
        else
        {
            val += vec[r];
            ++r;
        }
    }
    return cnt;
}

template <typename T>
class Counter
{
public:
    unordered_map<T, ll> tbl_;
    ll max_cnt_ = 0;
    T max_key_;
    ll min_cnt_ = -1;
    T min_key_;

    Counter(const vector<T> &vec) {
        rep(i, len(vec)) {
            ll v = ++tbl_[vec[i]];
            if (max_cnt_ < v) {
                max_cnt_ = v;
                max_key_ = vec[i];
            }
        }
    }

    ll count(T key) {
        return tbl_[key];
    }

    T maxkey() {
        return max_key_;
    }

    ll maxcnt() {
        return max_cnt_;
    }

    T minkey() {
        if (min_cnt_ == -1) {
            mincnt();
        }
        return min_key_;
    }

    ll mincnt() {
        if (min_cnt_ == -1) {
            min_key_ = tbl_.begin()->first;
            min_cnt_ = tbl_.begin()->second;
            for(auto itr = tbl_.begin(); itr != tbl_.end(); itr++){
                if(min_cnt_ < itr->second) {
                    min_key_ = itr->first;
                    min_cnt_ = itr->second;
                }
            }
        }
        return min_cnt_;
    }
};

// 簡易二項係数
ll comb(ll n, ll k)
{
    ll v = 1;
    rep(i, k) v *= (n - i);
    rep(i, k) v /= (i + 1);
    return v;
}

// nが大きくてkが小さいときO(k) nが大きい時はllを使う。
ll combNbig(ll n, ll k) {
    if(k < 0 || n < k) return 0;
    ll ret = 1;
    for(ll i = 1; i <= k; ++i) {
        ret *= n--;
        ret /= i;
    }
    return ret;
}

ll combNbig(ll n, ll k, ll m) {
    if(k < 0 || n < k) return 0;
    ll ret = 1;
    for(ll i = 1; i <= k; ++i) {
        ret = mod_mul(ret, n--, m);
        ret = mod_div(ret, i, m);
    }
    return ret % m;
}

// dはaとbの最小公倍数、xとyはax + by = gcd(a, b)を満たすx, y
ll extgcd(ll a, ll b, ll &x, ll &y)
{
    ll d = a;
    if(b != 0) {
        d = extgcd(b, a % b, y, x);
        y -= (a / b) * x;
    } else {
        x = 1;
        y = 0;
    }
    return d;
}

ll mysqrt(ll n) {
    ll ok = 0, ng = n + 1;
    while (ng - ok > 1) {
        ll mid = (ng + ok) >> 1;
        if (mid * mid <= n) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    return ok;
}

ll det2(const vvll &mat) {
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0];
}

// 約数個数列挙(MAXNまで)
vll divisors_count(ll MAXN = 1000000)
{
    vll div = vll(MAXN + 1, 0);
    rrep(n, MAXN) repsp(m, n, MAXN + 1, n) {
        div[m] += 1;
    }
    return div;
}

// 約数列挙
vll make_divisors(ll n) {
    vll divisors;
    for(ll i = 1; i * i <= n; ++i) {
        if(n % i == 0) {
            divisors.pb(i);
            if(i != n / i) {
                divisors.pb(n / i);
            }
        }
    }
    return divisors;
}

// N以下の素数列挙(Nはせいぜい10^7くらいまで)
inline vll eratosthenes(ll N) {
    vll ps;
    vector<bool> primes(N + 1);
    rep(i, len(primes)) primes[i] = true;
    primes[0] = primes[1] = false;
    rep(i, len(primes)) {
        if (primes[i]) {
            ps.pb(i);
            for (ull j = i + i; j < len(primes); j += i) {
                primes[j] = false;
            }
        }
    }
    return ps;
}

// 高速素数判定
bool suspect(ll a, ll s, ll d, ll md){
    ll x = 1, xx = a, one = x, minusone = md - 1;
    while(d > 0){
        if(d & 1) x = mod_mul(x, xx, md);
        xx = mod_mul(xx, xx, md);
        d >>= 1;
    }
    if ((x % md) == (one % md)) return true;
    for (ll r = 0; r < s; ++r) {
        if((x % md) == (minusone % md)) return true;
        x = mod_mul(x, x, md);
    }
    return false;
}

// 64ビット整数までの高速素数判定
bool is_prime_miller_rabin(ll n){
    if (n <= 1 || (n > 2 && n % 2 == 0)) return false;
    ll d = n - 1, s = 0;
    while (!(d&1)) {++s; d >>= 1;}
    vll v = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};
    if(n < 4759123141LL) v = {2, 7, 61};
    for (auto &&p : v) {
        if(p >= n) break;
        if(!suspect(p, s, d, n)) return false;
    }
    return true;
}

// 高速素数判定
bool is_prime(ll p, int k = 50)
{
    ll q = abs(p);
    if (q == 2) return true;
    if ((q < 2) || ((q & 1) == 0)) return false;

    ll d = (q - 1) >> 1;
    while ((d & 1) == 0) d >>= 1;

    static std::random_device rd;
    static std::mt19937_64 engine(rd());
    std::uniform_int_distribution<ll> distr(1, q - 1);
    rep(i, k){
        ll a = distr(engine);
        ll t = d;
        ll y = mod_bipow(a, t, q);
        while ((t != q - 1) && (y != 1) && (y != q - 1))
        {
            y = mod_bipow(y, 2, q);
            t <<= 1;
        }
        if ((y != q - 1) && ((t & 1) == 0)) return false;
    }
    return true;
}

// 素因数分解
umpll prime(ll m) {
    umpll pf;
    ll limit = sqrt(m) + 1;
    for(ll i = 2; i < limit; ++i) {
        while (m % i == 0) {
            pf[i] = pf[i] + 1;
            m /= i;
        }
    }
    if (m > 1) {
        pf[m] = 1;
    }
    return pf;
}

// 高速素因数分解(MAXNの範囲まで)
class Prime
{
public:
    static vll sieve; // 何回もPrimeのインスタンスを生成するときはstaticをはずして、下の実体もコメントアウトする。
    Prime(ll MAXN = 10000000) {
        rep(i, MAXN + 1) sieve.pb(i);
        ll p = 2;
        while (p * p <= MAXN) {
            if (sieve[p] == p) {
                repsp(q, 2 * p, MAXN + 1, p) {
                    if (sieve[q] == q) sieve[q] = p;
                }
            }
            p += 1;
        }
    }

    Counter<ll> prime(ll n) {
        if (n == 1) return Counter<ll>(vll());
        vll tmp;
        while (n > 1) {
            tmp.pb(sieve[n]);
            n = (ll)(n / sieve[n]);
        }
        return Counter<ll>(tmp);
    }
};
vll Prime::sieve = vll();

ll LIS(const vector<ll> &a, bool strict = true) // trueのとき厳密に増加する列
{
    vll lis;
    for(auto &p : a) {
        vll::iterator it;
        if(strict) it = lower_bound(all(lis), p);
        else it = upper_bound(all(lis), p);
        if(end(lis) == it) lis.emplace_back(p);
        else *it = p;
    }
    return len(lis);
}

ll randint(ll l, ll r)
{
    static random_device rnd;
    static mt19937_64 mt(rnd());
    uniform_int_distribution<> rand(l, r - 1);
    return rand(mt);
}

// 「#」がもの、「.」が何もないとすると、一回り周辺を「outside」で埋める
// マップを作成する。「.」が0で「#」が1を表す
inline vvll create_map(int h, int w, ll outside = 0)
{
    vs mp = in_vs(h);
    vvll tbl = init_tbl(h + 2, w + 2, outside);
    rrep(i, h) rrep(j, w) {
        tbl[i][j] = mp[i - 1][j - 1] == '.' ? 0 : 1;
    }
    return tbl;
}

inline bool substrcheck(const string &in, const string &ptn)
{
    boyer_moore_searcher searcher(all(ptn));
    auto it = search(all(ptn), searcher);
    return it != in.end();
}

// nCkをmで割った余りを求める
class Combination {
    const ll n_;
    const ll m_;
    vll facts_;
    vll inv_facts_;
public:
    Combination(ll N, ll mod) : n_(2 * N), m_(mod), facts_(n_ + 1), inv_facts_(n_ + 1) {
        rep(i, n_ + 1) facts_[i] = i == 0 ? 1 : mod_mul(facts_[i - 1], i, m_);
        for (ll i = n_; i >= 0; i--) inv_facts_[i] = i == n_ ? mod_inv(facts_[n_], m_) : mod_mul(inv_facts_[i + 1], i + 1, m_);   // (i!)^{-1}=((i+1)!)^{-1}*(i+1)
    }
    ll nPr(ll n, ll r) {
        return mod_mul(facts_[n], inv_facts_[n - r], m_);
    }
    ll nCr(ll n, ll r) {
        return mod_mul(facts_[n], mod_mul(inv_facts_[r], inv_facts_[n - r], m_), m_);
    }
    ll nHr(ll n, ll r) {
        return nCr(n + r - 1, r);
    }
    ll catalan(ll n) { // https://ja.wikipedia.org/wiki/%E3%82%AB%E3%82%BF%E3%83%A9%E3%83%B3%E6%95%B0
        return mod_mul(nCr(2 * n, n), mod_inv(n + 1, m_), m_);
    }
    // カタラン数・・・(2n C n)/(n + 1) = (2n C n) - (2n C n-1)
    // c0 = 1, c_n = rep(i, n) c[i] * c[n - i - 1]
    // c0から順に1,1,2,5,14,42,132,429,1430,...
};

ll max_cnt_interval_scheduling(vvll l) // コピーが実行される
{
    SORT_IDX(l, 1);
    ll r1 = l[0][1];
    ll cnt = 1;
    reps(i, 1, len(l)) {
        ll l1 = l[i][0], r2 = l[i][1];
        if (l1 >= r1) {
            cnt += 1;
            r1 = r2;
        }
    }
    return cnt;
}

class IntegralImage {
public:
    vvll data_;
    IntegralImage(ull H, ull W) : data_(H + 1, vll(W + 1, 0)) {}

    void add(ull h, ull w, ll z) {
        ++h, ++w;
        if(h >= len(data_) || w >= len(data_[0])) return;
        data_[h][w] += z;
    }

    void build() {
        for(ull i = 1; i < len(data_); i++) {
            for(ull j = 1; j < len(data_[i]); j++) {
                data_[i][j] += data_[i][j - 1] + data_[i - 1][j] - data_[i - 1][j - 1];
            }
        }
    }

    // matrixの升目の添え字で考えるのではなく
    // matrixの格子点で左上、右下で囲われた領域の総和を求める
    ll get(int sh, int sw, int gh, int gw) {
        return (data_[gh][gw] - data_[sh][gw] - data_[gh][sw] + data_[sh][sw]);
    }
};

class UnionFind {
    ll n_;
    vll size_;
    vll par_;
    vll link_;

public:
    UnionFind(ll n) : n_(n), size_(n, 1), par_(n), link_(n) {
        iota(all(par_), 0);
        iota(all(link_), 0);
    }

    ll find(ll x) {
        while (par_[x] != x) {
            par_[x] = par_[par_[x]];
            x = par_[x];
        }
        return x;
    }

    ll operator[](ll x) { return find(x); }

    bool unite(ll x, ll y) {
        x = find(x);
        y = find(y);
        if (x == y) { return false; }
        if (y < x) swap(x, y);
        size_[x] += size_[y];
        size_[y] = 0;
        par_[y] = x;
        swap(link_[x], link_[y]);
        return true;
    }

    vll find_all() {
        vll A(n_);
        rep(i, n_) A[i] = find(i);
        return A;
    }

    vll members(ll x) {
        vll mems = vll{x};
        for (ll y = link_[x]; y != x; y = link_[y]) mems.pb(y);
        return mems;
    }

    ll size(ll x) {
        return size_[find(x)];
    }

    bool same(ll x, ll y) {
        return find(x) == find(y);
    }

    vll roots() {
        vll rs;
        rep(i, n_) if (size_[i] > 0) rs.pb(i);
        return rs;
    }

    ll group_count() {
        return len(roots());
    }

    unordered_map<ll, vll> all_group_members() {
        unordered_map<ll, vll> group_members;
        rep(member, n_) group_members[find(member)].pb(member);
        return group_members;
    }
};

class Graph
{
private:
    unordered_map<ll, vector<pll>> edges_;
    unordered_map<ll, vector<pll>> ignore_edges_;

    const ll V_;
    const bool dir_;
    const ll ansmod_;

    // dist(-1で初期化), cntは呼び出し元でN個分の配列を与えること。connect_vtxsは空のvectorでよい。
    void bfs_(ll sv, vll &dist, vll &connect_vtxs, vll &cnt, vll &root, ll search_depth = 1000000000)
    {
        if (dist[sv] != -1) return;
        dll q = dll();
        q.pb(sv);
        dist[sv] = 0;
        connect_vtxs.pb(sv);
        cnt[sv] = 1;
        while (len(q) > 0) {
            ll p = q[0];
            q.popleft();
            if (!EXIST(p, edges_)) continue;
            vector<pll> &evw = edges_[p];
            for (const auto& [ev, w] : evw) {
                bool isignore = false;
                rep(i, len(ignore_edges_[p])) {
                    const auto& [igev, igw] = ignore_edges_[p][i];
                    if (ev == igev && w == igw) {
                        isignore = true;
                    }
                }
                if (isignore) continue;

                if (dist[ev] != -1) {
                    if (dist[ev] == dist[p] + 1) {
                        cnt[ev] += cnt[p];
                        cnt[ev] %= ansmod_;
                    }
                    continue;
                }
                dist[ev] = dist[p] + 1;
                root[ev] = p;
                cnt[ev] = cnt[p];
                connect_vtxs.pb(ev);
                if (dist[ev] < search_depth)
                {
                    if (w == 0) q.pf(ev);
                    else q.pb(ev);
                }
            }
        }
    }

public:
    vll path_; // dfsでたどった経路
    vll traverse_path_; // dfsでたどり着けるノード順

    Graph(ll V, bool dir, ll ansmod = 1000000007) : V_(V), dir_(dir), ansmod_(ansmod){}

    void append_edge(ll sv, ll ev, ll weight = 1)
    {
        vector<pll> &u = edges_[sv];
        pll v = make_pair(ev, weight);
        u.pb(v);
        if (!dir_) {
            swap(sv, ev);
            vector<pll> &ru = edges_[sv];
            pll rv = make_pair(ev, weight);
            ru.pb(rv);
        }
    }

    void ignore_edge(ll sv, ll ev, ll weight = 1) {
        vector<pll> &u = ignore_edges_[sv];
        pll v = make_pair(ev, weight);
        u.pb(v);
        if (!dir_) {
            swap(sv, ev);
            vector<pll> &ru = ignore_edges_[sv];
            pll rv = make_pair(ev, weight);
            ru.pb(rv);
        }
    }

    void ignore_edge_clear() {
        ignore_edges_.clear();
    }

    auto bfs(ll sv, ll search_depth = 1000000000) {
        static vll dist(V_, -1);
        static vll connect_vtxs;
        static vll cnt(V_);
        static vll root(V_, -1);
        rep(i, len(connect_vtxs)) {
            dist[connect_vtxs[i]] = -1;
            cnt[connect_vtxs[i]] = 0;
            root[connect_vtxs[i]] = -1;
        }
        connect_vtxs.clear();
        bfs_(sv, dist, connect_vtxs, cnt, root, search_depth);
        return make_tuple(dist, connect_vtxs, cnt, root);
    }

    void dfs(ll sv, ll N)
    {
        path_.clear();
        traverse_path_.clear();
        vector<bool> reached = vector<bool>(N, false);
        dll q = dll();
        q.pb(sv);
        while (len(q) != 0 ) {
            ll p = q.back();
            q.popright();
            if (p >= 0) {
                reached[p] = true;
                path_.pb(p);
                traverse_path_.pb(p);
                if (EXIST(p, edges_)) {
                    vector<pll> &evw = edges_[p];
                    for (const auto& [ev, w] : evw) {
                        if (reached[ev]) continue;

                        bool isignore = false;
                        rep(i, len(ignore_edges_[p])) {
                            const auto& [igev, igw] = ignore_edges_[p][i];
                            if (ev == igev && w == igw) {
                                isignore = true;
                            }
                        }
                        if (isignore) continue;

                        q.pb(~p);
                        q.pb(ev);
                    }
                }
            }
            else path_.pb(~p);
        }
    }

    vll topo_sort(ll V)
    {
        heapqll q;
        vll to = vll(V);
        vll topo_vertex_list;
        repdict(u, vtxs, edges_) {
            for (const auto& [ev, w] : vtxs) {
                ++to[ev];
            }
        }
        rep(i, V) {
            if (to[i] != 0) continue;
            HEAPPUSH(q, i);
        }
        while (len(q) != 0) {
            ll v = HEAPPOP(q);
            topo_vertex_list.pb(v);
            for (const auto [ev, w] : edges_[v]) {
                --to[ev];
                if (to[ev]) continue;
                HEAPPUSH(q, ev);
            }
        }
        return topo_vertex_list;
    }
};

class GridMap
{
private:
    unordered_map<ll, vector<pll>> edges_;
    const ll H_;
    const ll W_;
    const ll ansmod_;
    vvll gridmap_;
    const vvll dirHWWeight_ = {{1, 0, 1}, {-1, 0, 1}, {0, 1, 1}, {0, -1, 1}}; // 十字
    // const vvll dirHWWeight_ = {{1, 0, 1}, {-1, 0, 1}, {0, 1, 1}, {0, -1, 1},
    //                           {1, 1, 1}, {-1, 1, 1}, {1, -1, 1}, {-1, -1, 1}}; // 全方向

    vvll build(ll H, ll W) {
        vvll tbl = vvll(H, vll(W, -1));
        rep(i, H) {
            string s = in_str();
            rep(j, W) {
                 tbl[i][j] = s[j] != '#' ? 0 : -1;
            }
        }
        return tbl;
    }

    ll getpos(ll h, ll w) {
        return h * W_ + w;
    }

    vll getposinv(ll pos) {
        return vll{(ll)(pos / W_), pos % W_};
    }

public:
    vll dist_;
    vll cnt_;
    vll connect_vtxs_;

    GridMap(ll H, ll W, ll ansmod = 1000000007) : H_(H), W_(W), ansmod_(ansmod) {
        gridmap_ = build(H, W);
        reset();
    }

    void reset() {
        dist_ = vll(H_ * W_, -1);
        cnt_ = vll(H_ * W_);
        connect_vtxs_.clear();
    }

    void bfs(ll sh, ll sw, ll search_depth = 1000000000) {
        if (gridmap_[sh][sw] == -1) return;
        ll pos = getpos(sh, sw);
        if (dist_[pos] != -1) return;
        dll q = dll();
        q.pb(pos);
        dist_[pos] = 0;
        connect_vtxs_.pb(pos);
        cnt_[pos] = 1;
        while (len(q) > 0) {
            ll p = q[0];
            q.popleft();
            vll ps = getposinv(p);
            vvll edges;
            for(const auto &dir: dirHWWeight_) {
                ll dh = dir[0], dw = dir[1], dweight = dir[2];
                ll posh = ps[0] + dh, posw = ps[1] + dw;
                ll tmpp = getpos(posh, posw);
                if (0 <= posh && posh < H_ && 0 <= posw && posw < W_) {
                    if (gridmap_[posh][posw] == -1) continue;
                    if (dist_[tmpp] == -1) edges.pb(vll{tmpp, dweight});
                }
                if(len(edges) == 0) continue;

                for (const auto &edge: edges) {
                    ll ev = edge[0], w = edge[1];
                    if (dist_[ev] == -1 || dist_[ev] == dist_[p] + 1) {
                        cnt_[ev] += cnt_[p];
                        cnt_[ev] %= ansmod_;
                    }
                    if (dist_[ev] != -1) continue;

                    dist_[ev] = dist_[p] + 1;
                    cnt_[ev] = cnt_[p];
                    connect_vtxs_.pb(ev);
                    if (dist_[ev] < search_depth)
                    {
                        if (w == 0) q.pf(ev);
                        else q.pb(ev);
                    }
                }
            }
        }
    }
};

class Dijkstra{
    class Edge{
    public:
        ll to_;
        ll cost_;
        Edge(ll to, ll cost) : to_(to), cost_(cost) {}
    };

    vector<vector<Edge>> G_;
    ll V_;
    const ll INF = LLONG_MAX;

public:
    vll d_;
    vll roots_;
    Dijkstra(ll V) : G_(vector<vector<Edge>>(V)), V_(V), d_(vll(V, INF)), roots_(vll(V, -1)) {}

    void append_edge(ll from, ll to, bool dir = false, ll cost = 1) {
        G_[from].pb(Edge(to, cost));
        if (!dir) {
            G_[to].pb(Edge(from, cost));
        }
    }

    void shortest_path(ll s) {
        priority_queue<pll, vector<pll>, greater<pll>> que;
        d_[s] = 0;
        que.push(make_pair(0, s));
        while (true) {
            if (len(que) == 0) break;
            const auto[cost, v] = que.top(); que.pop();
            if (d_[v] < cost) continue;
            rep (i, len(G_[v])) {
                auto e = G_[v][i];
                if (d_[e.to_] > d_[v] + e.cost_) {
                    d_[e.to_] = d_[v] + e.cost_;
                    roots_[e.to_] = v;
                    que.push(make_pair(d_[e.to_], e.to_));
                }
            }
        }
    }

    void reset() {
        d_ = vll(V_, INF);
        roots_ = vll(V_, -1);
    }
};

class WarshallFloyd {
private:
    unordered_map<ll, vvll> edges_;
    unordered_map<ll, unordered_map<ll, sll>> ignore_edges_;

    const ll V_;
    const bool dir_;
    const ll ansmod_;

public:
    WarshallFloyd(ll V, bool dir, ll ansmod = 1000000007) : V_(V), dir_(dir), ansmod_(ansmod){}

    void append_edge(ll sv, ll ev, ll weight = 1)
    {
        vvll &u = edges_[sv];
        vll v = {ev, weight};
        u.pb(v);
        if (!dir_) {
            swap(sv, ev);
            vvll &ru = edges_[sv];
            vll rv = {ev, weight};
            ru.pb(rv);
        }
    }

    void ignore_edge(ll sv, ll ev, ll weight = 1) {
        sll &uv = ignore_edges_[sv][ev];
        uv.insert(weight);
        if (!dir_) {
            swap(sv, ev);
            sll &ruv = ignore_edges_[sv][ev];
            ruv.insert(weight);
        }
    }

    void remove_ignore_edge(ll sv, ll ev, ll weight = 1) {
        if (!EXIST(sv, ignore_edges_))
            return;
        if (!EXIST(ev, ignore_edges_[sv]))
            return;
        sll &uv = ignore_edges_[sv][ev];
        uv.erase(weight);
        if (!dir_) {
            swap(sv, ev);
            sll &ruv = ignore_edges_[sv][ev];
            ruv.erase(weight);
        }
    }

    vvll calcdist()
    {
        auto const INF = LLONG_MAX;
        vvll d(V_, vll(V_, INF));
        rep(i, V_) d[i][i] = 0;
        repdict(k, v, edges_) rep(i, len(v)) {
            if (EXIST(k, ignore_edges_)) if (EXIST(v[i][0], ignore_edges_[k])) if (EXIST(v[i][1], ignore_edges_[k][v[i][0]])) continue;
            d[k][v[i][0]] = std::min(d[k][v[i][0]], v[i][1]);
        }
        rep(k, V_) rep(i, V_) rep(j, V_)
        {
            if (d[i][k] != INF && d[k][j] != INF)
                d[i][j] = std::min(d[i][j], d[i][k] + d[k][j]);
        }
        return d;
    }
};

namespace internal {
    // @param n `0 <= n`
    // @return minimum non-negative `x` s.t. `n <= 2**x`
    int ceil_pow2(int n) {
        int x = 0;
        while ((1U << x) < (unsigned int)(n)) x++;
        return x;
    }

    template <class T>
    using is_signed_int128 =
        typename std::conditional<std::is_same<T, __int128_t>::value ||
                                    std::is_same<T, __int128>::value,
                                std::true_type,
                                std::false_type>::type;

    template <class T>
    using is_unsigned_int128 =
        typename std::conditional<std::is_same<T, __uint128_t>::value ||
                                    std::is_same<T, unsigned __int128>::value,
                                std::true_type,
                                std::false_type>::type;

    template <class T>
    using make_unsigned_int128 =
        typename std::conditional<std::is_same<T, __int128_t>::value,
                                __uint128_t,
                                unsigned __int128>;

    template <class T>
    using is_integral = typename std::conditional<std::is_integral<T>::value ||
                                                    is_signed_int128<T>::value ||
                                                    is_unsigned_int128<T>::value,
                                                std::true_type,
                                                std::false_type>::type;

    template <class T>
    using is_signed_int = typename std::conditional<(is_integral<T>::value &&
                                                    std::is_signed<T>::value) ||
                                                        is_signed_int128<T>::value,
                                                    std::true_type,
                                                    std::false_type>::type;

    template <class T>
    using is_unsigned_int =
        typename std::conditional<(is_integral<T>::value &&
                                std::is_unsigned<T>::value) ||
                                    is_unsigned_int128<T>::value,
                                std::true_type,
                                std::false_type>::type;

    template <class T>
    using to_unsigned = typename std::conditional<
        is_signed_int128<T>::value,
        make_unsigned_int128<T>,
        typename std::conditional<std::is_signed<T>::value,
                                std::make_unsigned<T>,
                                std::common_type<T>>::type>::type;

    template <class T>
    using is_signed_int_t = std::enable_if_t<is_signed_int<T>::value>;

    template <class T>
    using is_unsigned_int_t = std::enable_if_t<is_unsigned_int<T>::value>;

    template <class T> using to_unsigned_t = typename to_unsigned<T>::type;
}  // namespace internal

template <class T> struct fenwick_tree {
public:
    fenwick_tree() : _n(0) {}
    fenwick_tree(int n) : _n(n), data(n) {}

    void add(int p, T x) {
        assert(0 <= p && p < _n);
        p++;
        while (p <= _n) {
            data[p - 1] += x;
            p += p & -p;
        }
    }

    T sum(int l, int r) { // [l, r)
        assert(0 <= l && l <= r && r <= _n);
        return l == 0 ? sum(r) : sum(r) - sum(l);
    }

  private:
    int _n;
    std::vector<T> data;

    T sum(int r) {
        T s = 0;
        while (r > 0) {
            s += data[r - 1];
            r -= r & -r;
        }
        return s;
    }
};

class Bit
{
public:
    fenwick_tree<ll> ft;
    Bit(ll n = 0) : ft(n){}

    ll sum(ll i) { // [0, i)
        return ft.sum(0, i);
    }

    ll sum(ll l, ll r) { // [l, r)
        return ft.sum(l, r);
    }

    void add(ll i, ll x) {
        ft.add(i, x);
    }

    void rangeadd(ll l, ll r, ll x) { // [l, r)
        ft.add(r, -x);
        ft.add(l, x);
    }

    ll inversion(const vll &vec) {
        ft = fenwick_tree<ll>(MAX(vec) + 1);
        ll val = 0;
        rep(i, len(vec)) {
            ft.add(vec[i], 1);
            val += i + 1 - sum(vec[i] + 1);
        }
        return val;
    }

    ll big_inversion(const vll &vec) {
        sll s = SET(vec);
        umpll d; ll idx = 0;
        repset(x, s) {
            d[x] = idx++;
        }
        vll v;
        rep(i, len(vec)) {
            v.pb(d[vec[i]]);
        }
        return inversion(v);
    }
};

template <typename T>
pair<unordered_map<T, ll>, vector<T>> compcoord(const vector<T> vec)
{
    set<T> s = SET(vec);
    unordered_map<T, ll> d;
    auto N = len(s);
    auto itr = s.begin();
    rep(i, N) {
        d[*itr] = i;
        ++itr;
    }
    vector<T> revd = vector<T>(N);
    repdict(k, v, d) {
        revd[v] = k;
    }
    return make_pair(d, revd);
}

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};



// https://howardhinnant.github.io/combinations.html
namespace howardhinnantdetail
{

// Rotates two discontinuous ranges to put *first2 where *first1 is.
//     If last1 == first2 this would be equivalent to rotate(first1, first2, last2),
//     but instead the rotate "jumps" over the discontinuity [last1, first2) -
//     which need not be a valid range.
//     In order to make it faster, the length of [first1, last1) is passed in as d1,
//     and d2 must be the length of [first2, last2).
//  In a perfect world the d1 > d2 case would have used swap_ranges and
//     reverse_iterator, but reverse_iterator is too inefficient.
template <class BidirIter>
void
rotate_discontinuous(BidirIter first1, BidirIter last1,
                     typename std::iterator_traits<BidirIter>::difference_type d1,
                     BidirIter first2, BidirIter last2,
                     typename std::iterator_traits<BidirIter>::difference_type d2)
{
    using std::swap;
    if (d1 <= d2)
        std::rotate(first2, std::swap_ranges(first1, last1, first2), last2);
    else
    {
        BidirIter i1 = last1;
        while (first2 != last2)
            swap(*--i1, *--last2);
        std::rotate(first1, i1, last1);
    }
}

// Rotates the three discontinuous ranges to put *first2 where *first1 is.
// Just like rotate_discontinuous, except the second range is now represented by
//    two discontinuous ranges: [first2, last2) + [first3, last3).
template <class BidirIter>
void
rotate_discontinuous3(BidirIter first1, BidirIter last1,
                      typename std::iterator_traits<BidirIter>::difference_type d1,
                      BidirIter first2, BidirIter last2,
                      typename std::iterator_traits<BidirIter>::difference_type d2,
                      BidirIter first3, BidirIter last3,
                      typename std::iterator_traits<BidirIter>::difference_type d3)
{
    rotate_discontinuous(first1, last1, d1, first2, last2, d2);
    if (d1 <= d2)
        rotate_discontinuous(std::next(first2, d2 - d1), last2, d1, first3, last3, d3);
    else
    {
        rotate_discontinuous(std::next(first1, d2), last1, d1 - d2, first3, last3, d3);
        rotate_discontinuous(first2, last2, d2, first3, last3, d3);
    }
}

// Call f() for each combination of the elements [first1, last1) + [first2, last2)
//    swapped/rotated into the range [first1, last1).  As long as f() returns
//    false, continue for every combination and then return [first1, last1) and
//    [first2, last2) to their original state.  If f() returns true, return
//    immediately.
//  Does the absolute mininum amount of swapping to accomplish its task.
//  If f() always returns false it will be called (d1+d2)!/(d1!*d2!) times.
template <class BidirIter, class Function>
bool
combine_discontinuous(BidirIter first1, BidirIter last1,
                      typename std::iterator_traits<BidirIter>::difference_type d1,
                      BidirIter first2, BidirIter last2,
                      typename std::iterator_traits<BidirIter>::difference_type d2,
                      Function& f,
                      typename std::iterator_traits<BidirIter>::difference_type d = 0)
{
    typedef typename std::iterator_traits<BidirIter>::difference_type D;
    using std::swap;
    if (d1 == 0 || d2 == 0)
        return f();
    if (d1 == 1)
    {
        for (BidirIter i2 = first2; i2 != last2; ++i2)
        {
            if (f())
                return true;
            swap(*first1, *i2);
        }
    }
    else
    {
        BidirIter f1p = std::next(first1);
        BidirIter i2 = first2;
        for (D d22 = d2; i2 != last2; ++i2, --d22)
        {
            if (combine_discontinuous(f1p, last1, d1-1, i2, last2, d22, f, d+1))
                return true;
            swap(*first1, *i2);
        }
    }
    if (f())
        return true;
    if (d != 0)
        rotate_discontinuous(first1, last1, d1, std::next(first2), last2, d2-1);
    else
        rotate_discontinuous(first1, last1, d1, first2, last2, d2);
    return false;
}

// A binder for binding arguments to call combine_discontinuous
template <class Function, class BidirIter>
class call_combine_discontinuous
{
    typedef typename std::iterator_traits<BidirIter>::difference_type D;
    Function f_;
    BidirIter first1_;
    BidirIter last1_;
    D d1_;
    BidirIter first2_;
    BidirIter last2_;
    D d2_;

public:
    call_combine_discontinuous(
                      BidirIter first1, BidirIter last1,
                      D d1,
                      BidirIter first2, BidirIter last2,
                      D d2,
                      Function& f)
        : f_(f), first1_(first1), last1_(last1), d1_(d1),
                 first2_(first2), last2_(last2), d2_(d2) {}

    bool operator()()
    {
        return combine_discontinuous(first1_, last1_, d1_, first2_, last2_, d2_, f_);
    }
};

// See combine_discontinuous3
template <class BidirIter, class Function>
bool
combine_discontinuous3_(BidirIter first1, BidirIter last1,
                        typename std::iterator_traits<BidirIter>::difference_type d1,
                        BidirIter first2, BidirIter last2,
                        typename std::iterator_traits<BidirIter>::difference_type d2,
                        BidirIter first3, BidirIter last3,
                        typename std::iterator_traits<BidirIter>::difference_type d3,
                        Function& f,
                        typename std::iterator_traits<BidirIter>::difference_type d = 0)
{
    typedef typename std::iterator_traits<BidirIter>::difference_type D;
    using std::swap;
    if (d1 == 1)
    {
        for (BidirIter i2 = first2; i2 != last2; ++i2)
        {
            if (f())
                return true;
            swap(*first1, *i2);
        }
        if (f())
            return true;
        swap(*first1, *std::prev(last2));
        swap(*first1, *first3);
        for (BidirIter i2 = std::next(first3); i2 != last3; ++i2)
        {
            if (f())
                return true;
            swap(*first1, *i2);
        }
    }
    else
    {
        BidirIter f1p = std::next(first1);
        BidirIter i2 = first2;
        for (D d22 = d2; i2 != last2; ++i2, --d22)
        {
            if (combine_discontinuous3_(f1p, last1, d1-1, i2, last2, d22, first3,
                                        last3, d3, f, d+1))
                return true;
            swap(*first1, *i2);
        }
        i2 = first3;
        for (D d22 = d3; i2 != last3; ++i2, --d22)
        {
            if (combine_discontinuous(f1p, last1, d1-1, i2, last3, d22, f, d+1))
                return true;
            swap(*first1, *i2);
        }
    }
    if (f())
        return true;
    if (d1 == 1)
        swap(*std::prev(last2), *first3);
    if (d != 0)
    {
        if (d2 > 1)
            rotate_discontinuous3(first1, last1, d1, std::next(first2), last2, d2-1, first3, last3, d3);
        else
            rotate_discontinuous(first1, last1, d1, first3, last3, d3);
    }
    else
        rotate_discontinuous3(first1, last1, d1, first2, last2, d2, first3, last3, d3);
    return false;
}

// Like combine_discontinuous, but swaps/rotates each combination out of
//    [first1, last1) + [first2, last2) + [first3, last3) into [first1, last1).
//    If f() always returns false, it is called (d1+d2+d3)!/(d1!*(d2+d3)!) times.
template <class BidirIter, class Function>
bool
combine_discontinuous3(BidirIter first1, BidirIter last1,
                       typename std::iterator_traits<BidirIter>::difference_type d1,
                       BidirIter first2, BidirIter last2,
                       typename std::iterator_traits<BidirIter>::difference_type d2,
                       BidirIter first3, BidirIter last3,
                       typename std::iterator_traits<BidirIter>::difference_type d3,
                       Function& f)
{
    typedef call_combine_discontinuous<Function&, BidirIter> F;
    F fbc(first2, last2, d2, first3, last3, d3, f);  // BC
    return combine_discontinuous3_(first1, last1, d1, first2, last2, d2, first3, last3, d3, fbc);
}

// See permute
template <class BidirIter, class Function>
bool
permute_(BidirIter first1, BidirIter last1,
         typename std::iterator_traits<BidirIter>::difference_type d1,
         Function& f)
{
    using std::swap;
    switch (d1)
    {
    case 0:
    case 1:
        return f();
    case 2:
        if (f())
            return true;
        swap(*first1, *std::next(first1));
        return f();
    case 3:
        {
        if (f())
            return true;
        BidirIter f2 = std::next(first1);
        BidirIter f3 = std::next(f2);
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*first1, *f3);
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*first1, *f2);
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*f2, *f3);
        return f();
        }
    }
    BidirIter fp1 = std::next(first1);
    for (BidirIter p = fp1; p != last1; ++p)
    {
        if (permute_(fp1, last1, d1-1, f))
            return true;
        std::reverse(fp1, last1);
        swap(*first1, *p);
    }
    return permute_(fp1, last1, d1-1, f);
}

// Calls f() for each permutation of [first1, last1)
// Divided into permute and permute_ in a (perhaps futile) attempt to
//    squeeze a little more performance out of it.
template <class BidirIter, class Function>
bool
permute(BidirIter first1, BidirIter last1,
        typename std::iterator_traits<BidirIter>::difference_type d1,
        Function& f)
{
    using std::swap;
    switch (d1)
    {
    case 0:
    case 1:
        return f();
    case 2:
        {
        if (f())
            return true;
        BidirIter i = std::next(first1);
        swap(*first1, *i);
        if (f())
            return true;
        swap(*first1, *i);
        }
        break;
    case 3:
        {
        if (f())
            return true;
        BidirIter f2 = std::next(first1);
        BidirIter f3 = std::next(f2);
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*first1, *f3);
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*first1, *f2);
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*f2, *f3);
        if (f())
            return true;
        swap(*first1, *f3);
        }
        break;
    default:
        BidirIter fp1 = std::next(first1);
        for (BidirIter p = fp1; p != last1; ++p)
        {
            if (permute_(fp1, last1, d1-1, f))
                return true;
            std::reverse(fp1, last1);
            swap(*first1, *p);
        }
        if (permute_(fp1, last1, d1-1, f))
            return true;
        std::reverse(first1, last1);
        break;
    }
    return false;
}

// Creates a functor with no arguments which calls f_(first_, last_).
//   Also has a variant that takes two It and ignores them.
template <class Function, class It>
class bound_range
{
    Function f_;
    It first_;
    It last_;
public:
    bound_range(Function f, It first, It last)
        : f_(f), first_(first), last_(last) {}

    bool
    operator()()
    {
        return f_(first_, last_);
    }

    bool
    operator()(It, It)
    {
        return f_(first_, last_);
    }
};

// A binder for binding arguments to call permute
template <class Function, class It>
class call_permute
{
    typedef typename std::iterator_traits<It>::difference_type D;
    Function f_;
    It first_;
    It last_;
    D d_;
public:
    call_permute(Function f, It first, It last, D d)
        : f_(f), first_(first), last_(last), d_(d) {}

    bool
    operator()()
    {
        return permute(first_, last_, d_, f_);
    }
};

}  // detail

template <class BidirIter, class Function>
Function
for_each_combination(BidirIter first, BidirIter last,
                     BidirIter mid, Function f)
{
    howardhinnantdetail::bound_range<Function&, BidirIter> wfunc(f, first, mid);
    howardhinnantdetail::combine_discontinuous(first, mid, std::distance(first, mid),
                                  mid, last, std::distance(mid, last),
                                  wfunc);
    return f;
}

class BitwiseFullSearch
{
public:
    ll count_;
    std::function<void(const vll &ptn, ll &count)> checkcount_; // カウントするロジックのラムダ式を突っ込む。

    BitwiseFullSearch(std::function<void(const vll &ptn, ll &count)> f) : count_(0), checkcount_(f) {}
    // ここは触らなくてよい(パターンを列挙しているだけ)
    bool operator()(vll::iterator it1, vll::iterator it2)
    {
        vll ptn;
        while (it1 != it2)
        {
            ptn.pb(*it1);
            ++it1;
        }
        checkcount_(ptn, count_);
        return false;
    }
};

ll _comb_ptn_count(ll R, const std::function<void(const vll &ptn, ll &count)> &f, vll &_A_) {
    auto B = BitwiseFullSearch(f);
    vll::iterator _R_ = _A_.begin() + R;
    B = for_each_combination(all(_A_), _R_, B);
    return B.count_;
}

ll comb_ptn_count(ll N, ll R, const std::function<void(const vll &ptn, ll &count)> &f) {
    SETPERM(_A_, N);
    return _comb_ptn_count(R, f, _A_);
}

vvll get_comb_ptn(ll N, ll R) {
    vvll cb;
    auto f = [&](const vll &ptn, ll &count)
    {
        UNUSED(count);
        cb.pb(ptn);
    };
    comb_ptn_count(N, R, f);
    return cb;
}

ll comb_allptn_count(ll N, const std::function<void(const vll &ptn, ll &count)> &f) {
    ll cnt = 0;
    SETPERM(_A_, N);
    rep(r, N + 1) {
        cnt += _comb_ptn_count(r, f, _A_);
    }
    return cnt;
}

vvll get_comb_allptn(ll N) {
    vvll cb;
    auto f = [&](const vll &ptn, ll &count)
    {
        UNUSED(count);
        cb.pb(ptn);
    };
    comb_allptn_count(N, f);
    return cb;
}

template <class S, S (*op)(S, S), S (*e)()> struct segtree {
  public:
    segtree() : segtree(0) {}
    segtree(int n) : segtree(std::vector<S>(n, e())) {}
    segtree(const std::vector<S>& v) : _n(int(v.size())) {
        log = internal::ceil_pow2(_n);
        size = 1 << log;
        d = std::vector<S>(2 * size, e());
        for (int i = 0; i < _n; i++) d[size + i] = v[i];
        for (int i = size - 1; i >= 1; i--) {
            update(i);
        }
    }

    void set(int p, S x) { // 0-origin
        assert(0 <= p && p < _n);
        p += size;
        d[p] = x;
        for (int i = 1; i <= log; i++) update(p >> i);
    }

    S get(int p) { // 0-origin
        assert(0 <= p && p < _n);
        return d[p + size];
    }

    S prod(int l, int r) { // 0-origin [l, r)
        assert(0 <= l && l <= r && r <= _n);
        S sml = e(), smr = e();
        l += size;
        r += size;

        while (l < r) {
            if (l & 1) sml = op(sml, d[l++]);
            if (r & 1) smr = op(d[--r], smr);
            l >>= 1;
            r >>= 1;
        }
        return op(sml, smr);
    }

    S all_prod() { return d[1]; }

    template <bool (*f)(S)> int max_right(int l) { // 引数も戻り値も0-origin
        return max_right(l, [](S x) { return f(x); });
    }

    // lより右側でfを満たす最大の右位置を取得
    template <class F> int max_right(int l, F f) { // 引数も戻り値も0-origin
        assert(0 <= l && l <= _n);
        assert(f(e()));
        if (l == _n) return _n;
        l += size;
        S sm = e();
        do {
            while (l % 2 == 0) l >>= 1;
            if (!f(op(sm, d[l]))) {
                while (l < size) {
                    l = (2 * l);
                    if (f(op(sm, d[l]))) {
                        sm = op(sm, d[l]);
                        l++;
                    }
                }
                return l - size;
            }
            sm = op(sm, d[l]);
            l++;
        } while ((l & -l) != l);
        return _n;
    }

    template <bool (*f)(S)> int min_left(int r) { // 引数も戻り値も0-origin
        return min_left(r, [](S x) { return f(x); });
    }

    // rより左側でfを満たす最小の左位置を取得
    template <class F> int min_left(int r, F f) { // 引数も戻り値も0-origin
        assert(0 <= r && r <= _n);
        assert(f(e()));
        if (r == 0) return 0;
        r += size;
        S sm = e();
        do {
            r--;
            while (r > 1 && (r % 2)) r >>= 1;
            if (!f(op(d[r], sm))) {
                while (r < size) {
                    r = (2 * r + 1);
                    if (f(op(d[r], sm))) {
                        sm = op(d[r], sm);
                        r--;
                    }
                }
                return r + 1 - size;
            }
            sm = op(d[r], sm);
        } while ((r & -r) != r);
        return 0;
    }

  private:
    int _n, size, log;
    std::vector<S> d;

    void update(int k) { d[k] = op(d[2 * k], d[2 * k + 1]); }
};

template <class S,
          S (*op)(S, S),
          S (*e)(),
          class F,
          S (*mapping)(F, S),
          F (*composition)(F, F),
          F (*id)()>
struct lazy_segtree {
  public:
    lazy_segtree() : lazy_segtree(0) {}
    lazy_segtree(int n) : lazy_segtree(std::vector<S>(n, e())) {}
    lazy_segtree(const std::vector<S>& v) : _n(int(v.size())) {
        log = internal::ceil_pow2(_n);
        size = 1 << log;
        d = std::vector<S>(2 * size, e());
        lz = std::vector<F>(size, id());
        for (int i = 0; i < _n; i++) d[size + i] = v[i];
        for (int i = size - 1; i >= 1; i--) {
            update(i);
        }
    }

    void set(int p, S x) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        d[p] = x;
        for (int i = 1; i <= log; i++) update(p >> i);
    }

    S get(int p) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        return d[p];
    }

    S prod(int l, int r) {
        assert(0 <= l && l <= r && r <= _n);
        if (l == r) return e();

        l += size;
        r += size;

        for (int i = log; i >= 1; i--) {
            if (((l >> i) << i) != l) push(l >> i);
            if (((r >> i) << i) != r) push(r >> i);
        }

        S sml = e(), smr = e();
        while (l < r) {
            if (l & 1) sml = op(sml, d[l++]);
            if (r & 1) smr = op(d[--r], smr);
            l >>= 1;
            r >>= 1;
        }

        return op(sml, smr);
    }

    S all_prod() { return d[1]; }

    void apply(int p, F f) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        d[p] = mapping(f, d[p]);
        for (int i = 1; i <= log; i++) update(p >> i);
    }
    void apply(int l, int r, F f) {
        assert(0 <= l && l <= r && r <= _n);
        if (l == r) return;

        l += size;
        r += size;

        for (int i = log; i >= 1; i--) {
            if (((l >> i) << i) != l) push(l >> i);
            if (((r >> i) << i) != r) push((r - 1) >> i);
        }

        {
            int l2 = l, r2 = r;
            while (l < r) {
                if (l & 1) all_apply(l++, f);
                if (r & 1) all_apply(--r, f);
                l >>= 1;
                r >>= 1;
            }
            l = l2;
            r = r2;
        }

        for (int i = 1; i <= log; i++) {
            if (((l >> i) << i) != l) update(l >> i);
            if (((r >> i) << i) != r) update((r - 1) >> i);
        }
    }

    template <bool (*g)(S)> int max_right(int l) {
        return max_right(l, [](S x) { return g(x); });
    }
    template <class G> int max_right(int l, G g) {
        assert(0 <= l && l <= _n);
        assert(g(e()));
        if (l == _n) return _n;
        l += size;
        for (int i = log; i >= 1; i--) push(l >> i);
        S sm = e();
        do {
            while (l % 2 == 0) l >>= 1;
            if (!g(op(sm, d[l]))) {
                while (l < size) {
                    push(l);
                    l = (2 * l);
                    if (g(op(sm, d[l]))) {
                        sm = op(sm, d[l]);
                        l++;
                    }
                }
                return l - size;
            }
            sm = op(sm, d[l]);
            l++;
        } while ((l & -l) != l);
        return _n;
    }

    template <bool (*g)(S)> int min_left(int r) {
        return min_left(r, [](S x) { return g(x); });
    }
    template <class G> int min_left(int r, G g) {
        assert(0 <= r && r <= _n);
        assert(g(e()));
        if (r == 0) return 0;
        r += size;
        for (int i = log; i >= 1; i--) push((r - 1) >> i);
        S sm = e();
        do {
            r--;
            while (r > 1 && (r % 2)) r >>= 1;
            if (!g(op(d[r], sm))) {
                while (r < size) {
                    push(r);
                    r = (2 * r + 1);
                    if (g(op(d[r], sm))) {
                        sm = op(d[r], sm);
                        r--;
                    }
                }
                return r + 1 - size;
            }
            sm = op(d[r], sm);
        } while ((r & -r) != r);
        return 0;
    }

  private:
    int _n, size, log;
    std::vector<S> d;
    std::vector<F> lz;

    void update(int k) { d[k] = op(d[2 * k], d[2 * k + 1]); }
    void all_apply(int k, F f) {
        d[k] = mapping(f, d[k]);
        if (k < size) lz[k] = composition(f, lz[k]);
    }
    void push(int k) {
        all_apply(2 * k, lz[k]);
        all_apply(2 * k + 1, lz[k]);
        lz[k] = id();
    }
};

// セグ木パターン
ll E0() { return (ll)0; }
ll E1() { return (ll)0; }
ll EM1() { return (ll)-1; }
ll EMAX() { return LLONG_MAX; }
ll EMIN() { return LLONG_MIN; }
ll EOR() { return (ll)0; }
ll EAND() { return (ll)(((ll)1 << (ll)62) - (ll)1); }
ll segmax(ll a, ll b) { return max(a, b); }
ll segmin(ll a, ll b) { return min(a, b); }
ll segand(ll a, ll b) { return a & b; }
ll segor(ll a, ll b) { return a | b; }
using SegTreeGCD = segtree<ll, gcd, E0>;
using SegTreeMaxE0 = segtree<ll, segmax, E0>; // 設定する要素の最小値が1のとき
using SegTreeMaxE1 = segtree<ll, segmax, E1>; // 設定する要素の最小値が2のとき
using SegTreeMaxEM1 = segtree<ll, segmax, EM1>; // 設定する要素の最小値が0のとき
using SegTreeMaxEMIN = segtree<ll, segmax, EMIN>;
using SegTreeMinE0 = segtree<ll, segmin, E0>;
using SegTreeMinE1 = segtree<ll, segmin, E1>;
using SegTreeMinEMAX = segtree<ll, segmin, EMAX>;
using SegTreeAnd = segtree<ll, segand, EAND>;
using SegTreeOr = segtree<ll, segor, EOR>;

// // 遅延セグ木パターン
// ll MPSUM(ll x, ll y) { return x + y; } // 区間加算用
// ll COMPSUM(ll x, ll y) { return x + y; } // 区間加算用
// ll IDSUM() { return 0LL; }

// // 最小値取得、区間加算(区間オフセット)
// using LazySegTreeGetMINChangeAdd = lazy_segtree<ll, segmin, EMAX, ll, MPSUM, COMPSUM, IDSUM>;
// // 最大値取得、区間加算(区間オフセット)
// using LazySegTreeGetMAXChangeAdd = lazy_segtree<ll, segmax, EMIN, ll, MPSUM, COMPSUM, IDSUM>;

// struct RangeSum { ll val; ll size; };
// vector<RangeSum> setTinit(vll &v) {
//     vector<RangeSum> r;
//     rep(i, len(v)) r.pb({v[i], 1});
//     return r;
// }
// RangeSum MPRANGESUM(RangeSum a, RangeSum b) { return {a.val + b.val, a.size + b.size};}
// RangeSum RANGESUME0() { return {0, 0}; }
// RangeSum MPADD(ll f, RangeSum x) { return {x.val + f * x.size, x.size}; }
// ll RANGEID() { return 0; }

// // 区間和取得、区間加算(区間オフセット)
// using LazySegTreeGetSUMChangeAdd = lazy_segtree<RangeSum, MPRANGESUM, RANGESUME0, ll, MPADD, COMPSUM, RANGEID>;

// const ll SEGID = LLONG_MAX - 14235;

// ll MPRANGEUPDATE(ll f, ll x) { return (f != SEGID) ? x : f; }

// RangeSum MPUPDATEADD(ll f, RangeSum x) {
//     if (f != SEGID) x.val = f * x.size;
//     return x;
// }
// ll COMPUPDATESUM(ll f, ll g) { return (f == SEGID ? g : f); }
// ll INITID() { return SEGID; }


// // 最小値取得、区間更新
// using LazySegTreeGetMINRangeUpdate = lazy_segtree<ll, segmin, EMAX, ll, MPRANGEUPDATE, COMPUPDATESUM, INITID>;
// // 最大値取得、区間更新
// using LazySegTreeGetMAXRangeUpdate = lazy_segtree<ll, segmax, EMIN, ll, MPRANGEUPDATE, COMPUPDATESUM, INITID>;
// // 区間和取得、区間更新
// using LazySegTreeGetSUMRangeUpdate = lazy_segtree<RangeSum, MPRANGESUM, RANGESUME0, ll, MPUPDATEADD, COMPUPDATESUM, INITID>;

template <typename T>
class BinTree {
    __gnu_pbds::tree<T, __gnu_pbds::null_type, less<T>, __gnu_pbds::rb_tree_tag, __gnu_pbds::tree_order_statistics_node_update> s;
public:
    BinTree() : s() {}
    BinTree(const vector<T> &v) : s(v) {}
    void add(const T &v) {
        s.insert(v);
    }
    void del(const T &v) {
        s.erase(v);
    }
    T getval(ll idx) {
        return *s.find_by_order(idx);
    }
    ll getidx(const T &val) {
        return s.order_of_key(val); // val未満の数が何個あるかわかる。(lower_bound)
    }
    void modify(const T &prevval, const T &newval) {
        del(prevval);
        add(newval);
    }
};

template <typename T>
T _Pivot(vector<T> &array, ll start, ll end);

template <typename T>
ll _Partition(vector<T> &array, ll start, ll end, const T &pivot)
{
    vector<T> lt, eq, mt;
    reps(i, start, end)
    {
        if (array[i] < pivot)
        {
            lt.pb(array[i]);
        }
        else if (array[i] == pivot)
        {
            eq.pb(array[i]);
        }
        else
        {
            mt.pb(array[i]);
        }
    }
    reps(i, start, start + len(lt))
    {
        array[i] = lt[i - start];
    }
    start += len(lt);
    ll ret = start;
    reps(i, start, start + len(eq))
    {
        array[i] = eq[i - start];
    }
    start += len(eq);
    reps(i, start, start + len(mt))
    {
        array[i] = mt[i - start];
    }
    return ret;
}

// [start, end)範囲のk番目(0-index)の値を取得。arrayは破壊的
template <typename T>
T get_kth_value(vector<T> &array, ll k, ll start, ll end)
{
    if (end - start <= 1)
        return array[start];
    ll pivotIndex = -1;
    do
    {
        T pivot = _Pivot(array, start, end);
        pivotIndex = _Partition(array, start, end, pivot);
        if (pivotIndex < k)
        {
            start = pivotIndex + 1;
        }
        else if (pivotIndex > k)
        {
            end = pivotIndex;
        }
    } while (pivotIndex != k);
    return array[k + start - 1];
}

template <typename T>
T _Median5(vector<T> array, ll start, ll end)
{
    reps(i, start, end)
    {
        reps(j, i + 1, end)
        {
            if (array[i] > array[j])
                swap(array[i], array[j]);
        }
    }
    return array[(end + start) / 2];
}

template <typename T>
T _Pivot(vector<T> &array, ll start, ll end)
{
    vector<T> medians;
    for (ll i = start; i < end; i += 5)
    {
        ll subStart = i;
        ll subEnd = min(i + 5, end);
        medians.pb(_Median5(array, subStart, subEnd));
    }
    ll n = len(medians);
    ll st = 0;
    ll ed = n;
    ll newk = n / 2;
    return get_kth_value(medians, newk, st, ed);
}


#include __FILE__
#endif


// 組み合わせで条件マッチしたものだけカウントするときのコード
// auto checkcount = [&](const vll &ptn, ll &count)
// {
//     // ptnに0からN-1からr個抽出したパターンが得られる
//     for (auto p : ptn)
//     {
//     }
//     // 条件を満たすものを確認
//     bool isok = true;
//     rep(j, M)
//     {
//         if (P[j] != (cnt[j] % 2))
//         {
//             isok = false;
//             break;
//         }
//     }
//     // 条件満たしていたらカウントする
//     if (isok)
//     {
//         count += 1;
//     }
// };

// return comb_allptn_count(N, checkcount);

