# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:23:23 2018

@author: kfgf831
"""
class collatz:
    
    @staticmethod
    def get_next(n):
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
            
            
    @staticmethod
    def get_sequence(start):
        out_sequence = []
        if start == 0:
            return out_sequence
        out_sequence.append(start)
        member = start
        while member != 1:
            member = int(collatz.get_next(member))
            out_sequence.append(member)
        return out_sequence
    
    @staticmethod
    def generate_sequence(start):
        n = start
        while n != 1:
            n = collatz.get_next(n)
            yield n
        

assert(collatz.get_sequence(1) == [1])
assert(collatz.get_sequence(2) == [2,1])
assert(collatz.get_sequence(3) == [3,10,5,16,8,4,2,1])
assert(collatz.get_next(1) == 1)
assert(collatz.get_next(2) == 1)
assert(collatz.get_next(3) == 10)
assert(collatz.get_next(4) == 2)
