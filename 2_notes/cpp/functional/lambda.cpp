#include <iostream>
#include <vector>





int main() {
  // no-dependancy lambda
  auto one = [](){
    return 1;
  };

  // lambda with params
  // trailing return type
  auto sum = [](int a, int b)->int {
    return a+b;
  };

  // lambda with selective captures (by reference)
  auto i = 5;
  auto mul5 = [&i](int a, int b) {
    return (a+b)*i;
  };

  // lambda with capture-all
  auto j = 6;
  auto mathy = [&]() {
    return i*j;
  };

  // "lambda" before c++11
  struct L {
    int operator() () {
      return 1;
    }
  };
  auto lamb = L {};



  std::cout << sum(one(), mul5(1, 2)) << "\n";
  std::cout << mathy() << "\n";
  std::cout << lamb() << "\n";
}
