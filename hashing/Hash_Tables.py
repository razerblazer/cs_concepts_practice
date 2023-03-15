from math import floor

#yes I am aware this already exists in python as a dictionary and there are libraries already implementing this in literally every other popular programming language but why recreate it from scratch lol 

class linkedlist:
    def __init__(self, key, value, nextval=None):
        self.key = key
        self.value = value
        self.nextval = nextval
"""        
essentially implement a python dictionary from scratch but creating different hashing functions
use singly linked list for chaining in the event of a collision
in the single most worst possible case where literally every hash translates to the same location in the array, every operation becomes O(n) linear time
this is why it is important to pick a hash function that will return a good spread and we can always scale up the size of the hash table depending on the number of elements being added to the table
"""
class hash_table:
#hash table size resizes when needed, default hash function is the division method
#welp just found out duplicates are not allowed
    def __init__(self, arr=[None]*100, hashtype=2):
        self.arr = arr
        self.hashtype = hashtype
        
    def add_value(self, key, value):
        hashval = self.hashfunctionconfig(self.hashtype, key)
        if self.arr[hashval] is None:
            self.arr[hashval] = linkedlist(key, value)
        else:
            currentnode = self.arr[hashval]
            while True:
                if currentnode.key == key:
                    return print(f"Key {key!s} already exists! We will not add that to the table.")
                if currentnode.nextval is None:
                    break
                currentnode = currentnode.nextval
            currentnode.nextval = linkedlist(key, value)
        print(f"The key value pair {key!s}:{value!s} has been added to the hash table!")
    
    def search(self, key):
        hashval = self.hashfunctionconfig(self.hashtype, key)
        if self.arr[hashval] is None:
            return print(f"{key!s} does not exist!")
        else:
            currentnode = self.arr[hashval]
            while True:
                if currentnode.key == key:
                    return print(f"The key {key!s} exists and it's value is {currentnode.value!s}!")
                if currentnode.nextval is None:
                    break
                currentnode = currentnode.nextval
        return print(f"{key!s} does not exist!")
    
    def delete(self, key):
        hashval = self.hashfunctionconfig(self.hashtype, key)
        if self.arr[hashval] is None:
            return print(f"{key!s} does not exist!")
        else:
            currentnode = self.arr[hashval]
            previousnode = None
            while True:
                if currentnode.key == key:
                    if previousnode is None:
                        self.arr[hashval] = None
                    else:
                        previousnode.nextval = None  #creating a copy of the currentnode will deviate it from the actual previous node we want
                    return print(f"The key value pair has been deleted!")
                if currentnode.nextval is None:
                    break
                previousnode = currentnode
                currentnode = currentnode.nextval
        return print(f"{key!s} does not exist!")
    
    def modify(self, key, newvalue):
        hashval = self.hashfunctionconfig(self.hashtype, key)
        if self.arr[hashval] is None:
            return print("key:value does not exist!")
        else:
            currentnode = self.arr[hashval]
            while True:
                if currentnode.key == key:
                    currentnode.value = newvalue
                    return print(f"The value at key {key!s} has been modified to {newvalue!s}!")
                if currentnode.next is None:
                    break
                currentnode = currentnode.nextval
        return print(f"key {key!s} does not exist!")
    
    def hashfunctionconfig(self, hashtype, key):
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
    #not a good idea to use where your key values will be numbers less than 10 and becomes more secure as the key value becomes larger
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
mydictionary = hash_table(hashtype=4)
mydictionary.add_value("hello", 0)
mydictionary.add_value(29,0)
mydictionary.add_value(40,1)
mydictionary.add_value(40,2)
mydictionary.search("ello")
mydictionary.search(40)
mydictionary.delete(40)
mydictionary.search(40)
mydictionary.delete(40)
mydictionary.delete(40)
mydictionary.modify(29, 10)
mydictionary.search(29)


