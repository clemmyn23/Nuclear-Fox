#include <stdexcept>
#include <iostream>

void err() {
  throw std::runtime_error {"runtime_error here"};
}

int main() {
  try {
    err();
  } catch (const std::exception &e) {
    std::cout << e.what() << "\n";
  }
}
