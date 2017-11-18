#include <type_traits>
#include <iostream>

template<typename T>
struct type1 {
    using type = T;
};

template<typename T>
struct type2 {
    using type = const T;
};

template<typename T, template<typename U> class typeclass = type1>
class fun_class {
public:
    using base_type = typename typeclass<T>::type;
    int i = 1;
};


int main() {
    using fun0_t = fun_class<int>;
    using fun1_t = fun_class<int, type1>;
    using fun2_t = fun_class<int, type2>;

    fun0_t f0;
    fun1_t f1;
    fun2_t f2;
    // if ((fun0.i == fun1.i) == fun2.i) {}
}
