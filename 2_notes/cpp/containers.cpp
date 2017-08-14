#include <iostream>
#include <vector>
#include <stack>
#include <tuple>

int main() {
    // simple integer vector
    std::vector<int> v1 = { 7, 6, 5, 4, 3 };
    v1.push_back(25);
    v1.push_back(41);
    for (const auto &i : v1) {
        std::cout << i << '\n';
    }

    // popping elements
    // const auto &ii = v1.back();         // get and return the last item in vector
    v1.pop_back();                      // removes the last item. no return
    v1.pop_back();
    for (const auto &i : v1) {
        std::cout << i << '\n';
    }


    // modifying elements in vector while iterating
    // for (auto &i : v1) {
    //     i = 1;
    //     std::cout << i << '\n';
    // }

    // std::stack<std::vector<int>> s1 = { 1, 2, 3 };

    std::stack<int> s1;
    if (!s1.empty()) {
        // reading top from empty stack will SIGSEGF
        // use empty() to check first
        std::cout << s1.top() << '\n';      // return the top element

    }
    s1.push(1);                         // push elem into stack. no return
    s1.pop();                           // pop elem from stack. no return
    s1.push(2);
    s1.push(3);
    // for (const auto &i : s1) {
    //     std::cout << i << '\n';
    // }
}
