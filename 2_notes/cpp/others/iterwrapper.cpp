#include <vector>
#include <iostream>

struct Node {
    std::vector<int> vec;
    std::vector<int>::iterator vec_itr;

    void begin() {
        vec_itr = vec.begin();
    }
    void next() {
        ++vec_itr;
    }
    bool end() {
        return (vec_itr == vec.end());
    }
    const int& value() const {
        return (*vec_itr);
    }
};


int main() {
    Node n1;
    n1.vec.emplace_back(1);
    n1.vec.emplace_back(2);
    n1.vec.emplace_back(3);
    n1.vec.emplace_back(4);

    // n1.begin();
    // std::cout << n1.value() << " " << n1.end() <<"\n";
    //
    // n1.next();
    // std::cout << n1.value() << " " << n1.end() <<"\n";
    //
    // n1.next();
    // std::cout << n1.value() << " " << n1.end() <<"\n";
    //
    // n1.next();
    // std::cout << n1.value() << " " << n1.end() <<"\n";


    for (n1.begin(); !n1.end(); n1.next()) {
        std::cout << n1.value() << "\n";
    }

    // for (auto &i : n1.vec) {
    //     std::cout << i << "\n";
    // }
}
