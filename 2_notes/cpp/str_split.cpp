#include <iostream>
// #include <stringstream>
#include <fstream>

int main() {

    // std::istringstream input = "hello world konnichiwa sekai";

    // std::ifstream in {"str.input"};
    std::ifstream in {"t1.input"};
    // std::istringstream str ;
    std::string line;
    while (in >> line) {

        std::cout << "==: " << line << '\n';
        // std::cout << line.find(' ') << '\n';
    }
//

}
