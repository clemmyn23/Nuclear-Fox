#include <iostream>

#include "friend.hpp"

BestFriend::BestFriend(const int name, const int num) :
num {num} {};



int main() {

    // BestFriend::BestFriend("aa", 1);
    // BestFriend b = BestFriend("bb", 2);
    BestFriend a {2, 1};


    std::cout << ' ' << '\n';
    return 0;
};
