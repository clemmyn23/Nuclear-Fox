#include <vector>
#include <ostream>
#include <type_traits>

// NOTES:
// do templated code in .hpp or .tpp files to allow for compile-time code generation.

template <typename T>
class SplitBucket {
private:
  std::vector<T> v1;
  std::vector<T> v2;
  bool selector =  true;

  void move(SplitBucket &&a, SplitBucket &&b) {
    a.v1 = std::move(b.v1);
    a.v2 = std::move(b.v2);
    a.selector = b.selector;
  }

public:
  static_assert(std::is_move_assignable<T>::value, "requires move");

  // Constructors
  SplitBucket() = default;

  // no copy because i am lazy
  SplitBucket(const SplitBucket&) = delete;

  // move
  SplitBucket(SplitBucket &&other) {
    if (this != &other)
      move(this, other);
  }

  // copy assign
  // move assign
  SplitBucket& operator=(SplitBucket &&other) {
    if (this != &other)
      move(this, other);
    return this;
  }


  // friend
  friend std::ostream& operator<<(std::ostream &os, const SplitBucket &sb) {
    for (const auto &i: sb.v1)
      os << i << ' ';
    for (const auto &i: sb.v2)
      os << i << ' ';
    return os;
  }

  // methods
  void insert(T &item) {
    if (selector) {
      v1.emplace_back(item);
    } else {
      v2.emplace_back(item);
    }
    selector = not selector;
  }


};



int main() {
  SplitBucket<int> sb {};

}
