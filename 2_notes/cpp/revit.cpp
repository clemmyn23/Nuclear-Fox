#include <iterator>
#include <iostream>
#include <algorithm>
#include <vector>

int main() {
	std::vector<int> a;
	auto it = a.end();
	// auto rt = std::make_reverse_iterator(it);
	auto rt = std::reverse_iterator<decltype(it)>(it);
    rt = rt;
}
