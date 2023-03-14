from math import floor
from copy import copy

class linkedlist:
    def __init__(self, key, value, nextval=None):
        self.key = key
        self.value = value
        self.nextval = nextval
#essentially implement a python dictionary from scratch but creating different hashing functions
#use singly linked list for chaining in the event of a collision

class hash_table:
#hash table size resizes when needed, default hash function is the division method
    def __init__(self, arr=[None]*100, hashtype=2):
        self.arr = arr
        self.hashtype = hashtype
        
    def add_value(self, key, value):
        hashval = self.hashfunctionconfig(self.hashtype)
        if self.arr[hashval] is None:
            self.arr[hashval] = linkedlist(key, value)
        else:
            currentnode = self.arr[hashval]
            while currentnode.nextval is not None:
                currentnode = currentnode.next
            currentnode.nextval = linkedlist(key, value)
        return f"The key value pair {key!s}:{value!s} has been added to the hash table!"
    
    def search(key, value):
        hashval = hashfunctionconfig(self.hashtype)
        if self.arr[hashval] is None:
            return "key:value does not exist!"
        else:
            currentnode = self.arr[hashval]
            while True:
                if currentnode.key == key and currentnode.value == value:
                    return "key:value exists!"
                if currentnode.next is None:
                    break
                currentnode = currentnode.next
        return "key:value does not exist!"
    
    def delete(key, value):
        hashval = hashfunction(self.hashtype)
        if self.arr[hashval] is None:
            return "key:value does not exist!"
        else:
            currentnode = self.arr[hashval]
            previousnode = None
            while True:
                if currentnode.key == key and currentnode.value == value:
                    if previousnode is None:
                        self.arr[hashval] = None
                    else:
                        previousnode.nextval = None
                    return f"The key value pair {key!s}:{value!s} has been deleted!"
                if currentnode.next is None:
                    break
                previousnode = copy(currentnode)
                currentnode = currentnode.nextval
        return "key:value does not exist!"
    
    def modify(key, value, newvalue):
        hashval = hashfunction(self.hashtype)
        if self.arr[hashval] is None:
            return "key:value does not exist!"
        else:
            currentnode = self.arr[hashval]
            while True:
                if currentnode.key == key and currentnode.value == value:
                    currentnode.value = newvalue
                    return f"The value in the key value pair {key!s}:{value!s} has been modified!"
                if currentnode.next is None:
                    break
                currentnode = currentnode.nextval
        return "key:value does not exist!"        
    
    def hashfunctionconfig(hashtype):
        if hashtype == 1:
            hashval = self.multiply(key)
        elif hashtype == 2:
            hashval = self.divide(key, 11)
        elif hashtype == 3:
            hashval = self.mid_square(key)
        elif hashtype == 4:
            hashval = self.folding_method(key, len(self.arr))        
        return hashval
    
    def createkeyint(self, key):
        val = 0
        if type(key) is str:
            for x in key:
                val += ord(x)
        elif type(key) is int:
            val = key
        else:
            raise Exception("Use either int or str for key datatype; anything else is unsuitable to be used as a key")
        return val
#hash function techniques; we will use number each hash function with a number to make sure each dictionary is configured with only one hash function
    
    #follows the formula of floor(M(kA mod 1)) where M is the size of the hash table, k is the key value and A is any constant where 0 < A < 1
    def multiply(self, key): #1
        val = self.createkeyint(key)
        return floor(len(self.arr) * (val*0.123 % 1))
    
    #ideal to avoid mods that are equivalent to the power of two, a prime that is not too close to powers of two are ideal
    def divide(self, key, mod): #2
        val = self.createkeyint(key)
        return val % mod
    
    #pretty simple hash function, we square the value of the key and then take the middle digits of the entire value as the hash(we will use the middle two digits here) 
    def mid_square(self, key): #3
        val = self.createkeyint(key)
        val = val**2
        val = str(val)
        middle = val[(len(val)//2) -1: (len(val)//2) +1]
        return int(middle)
        
    #split each key into single value number elements and add them all up to create your hash
    def folding_method(self, key, table_size): #4
        if len(self.arr) < table_size:
            self.arr + [None]* abs(len(self.arr) - table_size)
        val = 0
        if type(key) is str:
            for x in key:
                val += ord(x)
        elif type(key) is int:
            stringify = str(key)
            for num in stringify:
                val += int(num)
        else:
            raise Exception("Use either int or str for key datatype; anything else is unsuitable to be used as a key")
        return val % table_size
    

#testing
mydictionary = hash_table()
