#include <iostream>
#include <functional>


int f(int a, int b) {
  return a+b;
}

int main() {
  auto g = std::bind(f, 1, 2);
  std::cout << g() << '\n';
}
