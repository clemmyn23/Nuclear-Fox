#include <string>

class BestFriend {
public:

    // constructor
    BestFriend(const int name, const int num);

    // copy constructor
    BestFriend(const BestFriend&);


    // methods
    int getNum() const;

    // operators
    friend bool operator< (BestFriend &a, BestFriend &b);

private:
    int num;
    int age;
};
