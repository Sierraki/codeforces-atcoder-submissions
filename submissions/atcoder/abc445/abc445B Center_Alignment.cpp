/*
    Author    : MishkatIT
    Created   : Saturday 14-02-2026 18:25:57
*/

#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 42
#endif

using ll = long long;
using ld = long double;
const int mod = 1e9 + 7;
const int N = 2e5 + 10;
const int inf = 1e9;
const ll linf = 1e18;

void Solve() {
    int n;
    cin >> n;
    vector<string> v(n);
    int m = 0;
    for (auto& i : v) {
        cin >> i;
        m = max(m, (int)i.size());
    }
    for (int i = 0; i < n; i++) {
        int len = v[i].size();
        len = m - len; len /= 2;
        for (int x = 0; x < len; x++) cout << '.';
        cout << v[i];
        for (int x = 0; x < len; x++) cout << '.';
        cout << '\n';
    }
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int tc = 1;
    // cin >> tc;
    while (tc--) {
        Solve();
    }
    return 0;
}