# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:23:23 2018

@author: Adam Gołubowski
"""
class Collatz:
    """ Collatz conjecture sequences """
    @staticmethod
    def get_next(n):
        """ Generate next number in Collatz sequence for a given integer n """
        result = 0
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        elif n % 2 == 0:
            result = n / 2
        else:
            result = 3 * n + 1
        return result
            
    def __init__(self):
        self.sequence = []   
        
    def __call__(self, n):
        """ Generate a full sequence of numbers in Collatz sequence starting with integer n and ending in 1"""
        self.sequence = []
        if n == 0:
            return self.out_sequence
        self.sequence.append(n)
        member = n
        while member != 1:
            member = int(self.get_next(member))
            self.sequence.append(member)
        return self.sequence
    
    def generate_sequence(n):
        """ A generator for lazy iteration over Collatz conjecture sequence starting with integer n """
        next = n
        while next != 1:
            next = Collatz.get_next(next)
            yield next
        
c = Collatz()
assert(c(1) == [1])
assert(c(2) == [2,1])
assert(c(3) == [3,10,5,16,8,4,2,1])
assert(Collatz.get_next(1) == 1)
assert(Collatz.get_next(2) == 1)
assert(Collatz.get_next(3) == 10)
assert(Collatz.get_next(4) == 2)
