#include <vector>
#include <algorithm>
#include <iostream>

int main() {


    std::vector<int> vec {};
    vec.insert(std::upper_bound(vec.begin(), vec.end(), 9), 9);
    vec.insert(std::upper_bound(vec.begin(), vec.end(), 8), 8);
    vec.insert(std::upper_bound(vec.begin(), vec.end(), 7), 7);
    vec.insert(std::upper_bound(vec.begin(), vec.end(), 6), 6);
    vec.insert(std::upper_bound(vec.begin(), vec.end(), 5), 5);

    std::cout << "finding lt lower_bound index at ";
    auto lbit = std::lower_bound(vec.begin(), vec.end(), 4);
    std::cout << lbit - vec.begin() << '\n';

    std::cout << "finding smallest elem lower_bound at ";
    lbit = std::lower_bound(vec.begin(), vec.end(), 5);
    std::cout << lbit - vec.begin() << '\n';


    std::cout << "finding lt upper_bound index at ";
    auto ubit = std::upper_bound(vec.begin(), vec.end(), 4);
    std::cout << ubit - vec.begin() << '\n';

    std::cout << "finding smallest upper_bound index at ";
    ubit = std::upper_bound(vec.begin(), vec.end(), 5);
    std::cout << ubit - vec.begin() << '\n';



    std::cout << vec[0] << '\n';

    std::cout << "elem in vector:\n";
    for (auto &i : vec) {
        std::cout << i << ", ";
    }
    std::cout << '\n';

    std::cout << *(std::upper_bound(vec.begin(), vec.end(), 2)) << '\n';
    std::cout << "distance from begin() " << std::upper_bound(vec.begin(), vec.end(), 2) - vec.begin()
    << '\n';
}
