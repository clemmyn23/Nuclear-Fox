#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>

struct C {
    int& accessor() {
        return this->value;
    }
    int value;
};
void encapsulFun(const int& val) {
    std::cout << val << '\n';
}



template <typename T>
struct spv {
    std::vector<std::shared_ptr<T>> v1;
    bool contains(const T &target) const {
        return (std::find_if(v1.begin(), v1.end(),
            [&target](auto spt)->bool {
                return *spt == target;
            }
        ) != v1.end());
    }


    void pprint() const {
        for (auto &i : v1) {
            std::cout << *i << '\n';
            contains(*i);
        }
    }


};




int main() {
    C c;

    int a = c.accessor();
    const int b = c.accessor();

    encapsulFun(c.accessor());

    std::cout << a << '\n';
    std::cout << b << '\n';



    spv<int> s;
    auto sp1 = std::make_shared<int>(1);
    auto sp2 = std::make_shared<int>(2);
    auto sp3 = std::make_shared<int>(3);
    s.v1.emplace_back(sp1);
    s.v1.emplace_back(sp2);
    s.v1.emplace_back(sp3);
    s.pprint();



}
