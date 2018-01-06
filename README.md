# Collatz

## Overview
A Python program demonstrating [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture).

## Quick start
create Collatz sequences passing a starting value:
```python
c1 = Collatz(1)
c2 = Collatz(2)
c3 = Collatz(3)
c4 = Collatz(4)    
c5 = Collatz(5)
```

get sequences:
```python
assert(c1() == [1])
assert(c2() == [2,1])
assert(c3() == [3,10,5,16,8,4,2,1])
assert(c4() == [4,2,1])
assert(c5() == [5,16,8,4,2,1])
```

get sequence element at index:
```python
assert(c3[0] == 3)
assert(c3[3] == 16)
```

iterate over sequence:
```python
assert([x for x in c5] == [5,16,8,4,2,1])
```

lazy generation of sequence. Useful for large sequences. 
```python
assert([x for x in Collatz.generate_sequence(5)] == [5,16,8,4,2,1]) 
```

lazy generation is useful for large sequences or when you dont need all elements at once.
```python
for x in Collatz.generate_sequence(20):
    print(x)
20
10
5
16
8
4
2
1
```

get a successor of a number in a Collatz sequence
```python
assert(Collatz.successor(2) == 1)
assert(Collatz.successor(3) == 10)
```
