#include <iostream>
#include <vector>
#include <algorithm>


int main() {

    std::vector<int> v {1,2,3,4,5,6,7,8,9,10,11,12};

    for (auto &i : v) {
        std::cout << i << "\n";
    }


    std::cout << "=========================\n";

    auto oddfun = [](int &target)->bool {
        std::cout << "target: " << target << "\n";
        return (target%2 == 1);
    };
    auto odd_itr = std::find_if(v.begin(), v.end(), oddfun);

    while (odd_itr != v.end()) {
        std::cout << *odd_itr << "\n";
        odd_itr = std::find_if(++odd_itr, v.end(), oddfun);
    }

    std::cout << "=========================\n";


}
