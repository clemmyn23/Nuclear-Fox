#include <iostream>
#include <memory>

int main() {

    {
        int a = 123;
        auto sp = std::make_shared<int>(a);
        std::weak_ptr<int> wp1 = sp;

        // cannot assign object or ptrs into weak_ptr
        // std::weak_ptr<int> wp2 = a;      // fails to compile
    }

}
