#include <iostream>

#include "friend.hpp"

// BestFriend::BestFriend(const int name, const int num) :
// num {num} {
//     // empty
// };

// BestFriend::BestFriend(BestFriend&) {};

// class constructor definition here
Num::Num(int v) : value {v} {};
Num operator+ (Num& lhs, Num& rhs) {
    return Num {lhs.value + rhs.value};
};

std::ostream& operator<<(std::ostream &os, Num &n) {
    os << n.value;
    return os;
};







int main() {

    // BestFriend::BestFriend("aa", 1);
    // BestFriend b = BestFriend("bb", 2);
    // BestFriend a {2, 1};

    Num n1 {1};
    Num n2 {2};
    Num n3 = n1 + n2;
    Num n4 {};


    std::cout << "first " << n1 << '\n';
    std::cout << "second " << n2 << '\n';
    std::cout << "third " << n3 << '\n';
    std::cout << "fourth " << n4 << '\n';
    return 0;
};
