#include <iostream>

int main() {

    using namespace std;
    size_t n = 5;

    // "new" keyword is needed for dmem alloc of sizes
    // defined during runtime
    int *container = new int[n];


    cout << "super fun\n";
    int i = 0;
    for (; i < 5; ++i) {
        container[i] = 123;
        cout << container[i] << '\n';
    }


    cout << "== extra fun starts here\n";
    cout << container[-1] << '\n';  // under bound
    cout << container[i] << '\n';   // over bound
}
