# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:23:23 2018

@author: Adam Gołubowski
"""
class Collatz:
    """ Collatz conjecture sequences """
    @staticmethod
    def successor(n):
        """ Generate next number in Collatz sequence for a given integer n """
        result = 0
        if n == 0:
            result = 0
        elif n == 1:
            pass
        elif n % 2 == 0:
            result = n / 2
        else:
            result = 3 * n + 1
        return int(result)
            
    def __init__(self,n=0):
        self.sequence = []
        self.sequence = self.get_sequence(n)
        
    def __call__(self):
        """ Get Collatz sequence """ 
        return self.sequence
        
    def __len__(self):
        """ Length of Collatz sequence """
        return len(self.sequence)
    
    def __getitem__(self,key):
        """ Get element of Collatz sequence at a place specified by key """
        return self.sequence[key]
    
    def __iter__(self):
        """ Collatz sequence iterator """
        for member in self.sequence:
            yield int(member)
  
    @staticmethod
    def get_sequence(n):
        """ Generate a full sequence of numbers in Collatz sequence starting with integer n and ending in 1"""
        out_sequence = []
        if n == 0:
            return out_sequence
        out_sequence.append(n)
        member = n
        while member != 1:
            member = int(Collatz.successor(member))
            out_sequence.append(member)
        return out_sequence
    
    @staticmethod
    def generate_sequence(n):
        """ A generator for lazy iteration over Collatz conjecture sequence starting with integer n """
        member = n
        while member >= 1:
            yield int(member)
            member = Collatz.successor(member)
    
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

assert(Collatz.successor(1) == 0)
assert(Collatz.successor(2) == 1)
assert(Collatz.successor(3) == 10)
assert(Collatz.successor(4) == 2)

assert([x for x in c5] == [5,16,8,4,2,1])

assert([x for x in Collatz.generate_sequence(5)] == [5,16,8,4,2,1])
