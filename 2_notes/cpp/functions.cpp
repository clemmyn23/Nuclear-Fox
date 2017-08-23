#include <iostream>
// #include <fstream>



void printer(std::string str = "noparam printing") {
    std::cout << str << '\n';
}

int main(int argc, char **argv) {

    using namespace std;
    cout << "== regular function calls\n";
    printer("hello world 1");

    cout << "== function pointers (fn assign into var)\n";
    const auto &pf1 = printer;
    pf1("hello world 2");

    cout << "== self-involking lambda without args\n";
    ([]() { std::cout << "hello world 3\n"; })();

    cout << "== lambda assign\n";
    const auto &pf2 = [](std::string x) { std::cout << x << '\n'; };
    pf2("hello world 4");

    cout << "== no param\n";
    printer();
}
