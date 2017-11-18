# Core C++
- Types, pointers, references
- Exception handling / noexcept
- Constructors and initialiser lists
- Using statement
- Const

## Basic oop
- Friends
- Operator overloading

## Functional
- Lambdas
- Trailing return types
- Std::bind

## Utility
- Most vexing parse - ambiguity of "()" for constructor v. function call
- Narrowing - static_cast and losing bits
- Threads, mutexes, lock guards
- Std::forward
- moving - http://en.cppreference.com/w/cpp/language/value_category


# STL
Iterators - Input, output, forward, bidirectional, and random access
## Algorithms (http://en.cppreference.com/w/cpp/algorithm)
Especially useful (including their variants - eg. copy_if, copy_n)
Copy
Find
Transform
for_each
## Containers
Know the right time to use:
Vector
Array
Ordered / unordered set / map
List
Deque
Stack / queue (technically an adapter, not a container, but should know regardless)

# Memory management
Named / unnamed objects
Memory leak
owners
Double free
Smart pointers
RAII
Reference counting

# Templates
Function and class templates
Template specialisation
Type traits
Variadic templates

# Object Oriented Programming
Expect a fair amount of OOP, since you haven’t been examined on it in assignments
Access control
Inheritance
Vtables / virtual
Static / dynamic binding
Construction / destruction
Object slicing

# What will not be in the exam
Template metaprogramming
Custom iterators (you may be required to use iterators, but you will not be required to write your own)
Constexpr
Std::future
Extension topics
