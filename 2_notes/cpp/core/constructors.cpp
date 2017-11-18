
#include <vector>
#include <utility>

class Stub {


private:

  // swap that utilises std::move
  // - copy-swap idiom without the excess stores
  // - nothrow
  // - no performance penalty of self-assign guard
  void move(Stub &first, Stub &second) noexcept {
    first.size = std::move(second.size);
    first.data = std::move(second.data);
  }

  size_t size;
  std::vector<int> data;

public:

  // default noparam
  Stub() = default;

  // default specialised
  Stub(int s) {
    data = std::vector<int> (s);
    size = s;
  }

  // initlist
  Stub(std::initializer_list<int> ilist) {
    size = ilist.size();
    data = std::vector<int> (ilist);
  }

  // destuructor
  // - nothrow
  ~Stub() = default;


  // copy
  Stub(const Stub &other)
      : size {other.size}, data {other.data} {}

  // move
  // -nothrow
  Stub(Stub &&other) {
    move(*this, other);
  }

  // copy assign
  Stub& operator=(const Stub &other) {
    Stub temp (other);  // can throw
    move(*this, temp);
    return *this;
  }

  // move assign
  // - nothrow
  Stub& operator=(Stub &&other) {
    move(*this, other);   // nothrow
    return *this;
  }


};
