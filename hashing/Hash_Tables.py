#essentially implement a python dictionary from scratch but creating different hashing functions
#use singly linked list for chaining in the event of a collision

class hash_table:
#hash table size resizes when needed, default hash function is the division method
    def __init__(self, arr=[], hashtype=2):
        self.arr = arr
        self.hashtype = hashtype
        
    def add_value(self,key, value):
        return
    
#hash function techniques; we will use number each hash function with a number to make sure each dictionary is configured with only one hash function
    def multiply(self, key): #1
        return
    
#ideal to avoid mods that are equivalent to the power of two, a prime that is not too close to powers of two are ideal
    def divide(self, key, mod): #2
        val = 0
        if type(key) is str:
            for x in key:
                val += ord(x)
        elif type(key) is int:
            val = key
        else:
            raise Exception("Use either int or str for key datatype; anything else is unsuitable to be used as a key")
        return val % size
    
    def mid_square(self): #3
        return
    
    def folding_method(key, table_size): #4
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
    
class linkedlist:
    def __init__(self, key, value, nextval=None):
        self.key = key
        self.value = value
        self.nextval = nextval


#testing
mydictionary = hash_table()
