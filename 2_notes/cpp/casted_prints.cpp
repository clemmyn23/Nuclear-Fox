#include <iostream>

// casting:
// int --> double   not ok
// double --> int   ok

int main() {
    using namespace std;
    //
    // int a = 123;
    // cout << a << '\n';
    //
    // a = static_cast<double>(432.543);
    // cout << a << '\n';

    // std::cout.setf(std::ios::fixed, std::ios::floatfield);
    std::cout.setf(std::ios::fixed);
    std::cout.precision(3);

    double b = 324.523;
    cout << b << '\n';

    b = static_cast<int>(b);
    cout << b << '\n';
}
