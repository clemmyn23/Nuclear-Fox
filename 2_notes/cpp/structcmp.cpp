#include <set>
#include <iostream>
#include <memory>


template <typename T>
struct Node1  {
    struct Node2 {
        T subval1;
        Node2(T val) {subval1 = val;}
    };

    bool operator() (const Node2 &lhs, const Node2 &rhs) const {
        return lhs.subval1<rhs.subval1;
    }

};





template <typename T>
struct Node {
    T value1;
    T value2;
    Node(T v1, T v2) {
        value1 = v1;
        value2 = v2;
    }
};

template <typename T>
bool operator<(const Node<T> &lhs, const Node<T> &rhs) {
    return (lhs.value1+lhs.value2) < (rhs.value1+rhs.value2);
}

typedef std::shared_ptr<Node<int>> Node_spt;


int main() {

    std::set<Node1<int>, Node1<int>> subnodes ();
    
    // subnodes.insert();


    // Node1<int> base;
    // base.subnodes.insert(1);
    // base.subnodes.insert(4);
    // base.subnodes.insert(3);
    // base.subnodes.insert(2);
    // base.subnodes.insert(1);
    // for (auto &i : base.subnodes) {
    //     std::cout << i.subval1 << '\n';
    // }

    std::cout << "========================\n";




    Node<int> n1 {1, 2};    // 3
    Node<int> n2 {2, 3};    // 5
    Node<int> n3 {1, 1};    // 2
    Node<int> n4 {0, 1};    // 1
    Node<int> n5 {3, 1};    // 4

    Node_spt np1 = std::make_shared<Node<int>> (n1);
    Node_spt np2 = std::make_shared<Node<int>> (n2);
    Node_spt np3 = std::make_shared<Node<int>> (n3);
    Node_spt np4 = std::make_shared<Node<int>> (n4);
    Node_spt np5 = std::make_shared<Node<int>> (n5);

    std::cout << (np1 < np1) << '\n';

    std::cout << "==============\n";

    // std::cout << "n1<n2 " << (n1 < n2) << '\n';
    // std::cout << "n2<n1 " << (n2 < n1) << '\n';
    // std::cout << "n1<n3 " << (n1 < n3) << '\n';
    // std::set<Node<int>> s1 {n1, n2, n3, n4, n5};
    // for (auto &i : s1) {
    //     std::cout << (i.value1 + i.value2) << '\n';
    // }

    auto comp = [](const Node_spt &lhs, const Node_spt &rhs) {
        return (lhs->value1+lhs->value2) < (rhs->value1+rhs->value2);
    };

    std::set<Node_spt, decltype(comp)> s2 (comp);
    s2.insert(np1);
    s2.insert(np2);
    s2.insert(np3);
    s2.insert(np4);
    s2.insert(np5);
    for (auto &i : s2) {
        std::cout << (i->value1 + i->value2) << '\n';
    }

}
