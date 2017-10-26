#include <iostream>
#include <thread>
#include <chrono>

void f1() {
    std::cout << "exec f1()\n";
}

int main() {

    // spawning thread by passing functor
    std::thread t2 (f1);

    // spawning thread by passing lambda
    std::thread t1 { [](){
        std::cout << "exec lambda\n";
    } };

    // std::thread::detach separates thread of execution
    // from thread object.
    t2.detach();
    t1.detach();

    // std::thread::join blocks until thread finishes execution.
    // detached thread objects cannot call std::thread::join
    // check with std::thread::joinable
    // t1.join();
    // t2.join();


    // must wait till spawned threads exits first.
    // otherwise stdout is closed, no console prints.
    std::this_thread::sleep_for(std::chrono::seconds(5));
}
