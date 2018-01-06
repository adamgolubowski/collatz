# Collatz

A Python program demonstrating [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture).
```python
c1 = Collatz(1)
c2 = Collatz(2)
c3 = Collatz(3)
c4 = Collatz(4)    
c5 = Collatz(5)

assert(c1() == [1])
assert(c2() == [2,1])
assert(c3() == [3,10,5,16,8,4,2,1])
assert(c4() == [4,2,1])
assert(c5() == [5,16,8,4,2,1])

assert(c1[0] == 1)
assert(c3[0] == 3)
assert(c3[1] == 10)
assert(c3[3] == 16)

assert(Collatz.get_sequence(1) == [1])
assert(Collatz.get_sequence(2) == [2,1])
assert(Collatz.get_sequence(3) == [3,10,5,16,8,4,2,1])
assert(Collatz.get_sequence(4) == [4,2,1])
assert(Collatz.get_sequence(5) == [5,16,8,4,2,1])

assert(Collatz.successor(1) == 1)
assert(Collatz.successor(2) == 1)
assert(Collatz.successor(3) == 10)
assert(Collatz.successor(4) == 2)
```