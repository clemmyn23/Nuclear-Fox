#include <string>
//
// class BestFriend {
// public:
//
//     // constructor
//     BestFriend(const int name, const int num);
//
//     // copy constructor
//     BestFriend(const BestFriend&);
//
//
//     // methods
//     int getNum() const;
//
//     // operators
//     friend bool operator< (BestFriend &a, BestFriend &b);
//
// private:
//     int num;
//     int age;
// };
//


class Num {
public:

    // constructor declaration
    Num(int v = 5);

    // operator overloads
    // "friend" methods for accessing private class members
    friend Num operator+ (Num& lhs, Num& rhs);
    friend std::ostream& operator<< (std::ostream &os, Num &n);

private:
    const int value;
};
