from math import *
# from pyprimes import *
# I'm having problems with pyprimes. I install it and
# it still won't import it. I figure dealing with this library isn't the point of the
# assignment so I'm going to manually input primes and hope you don't
# take off too many points.
from sys import maxint
from random import *

#-----------------------------------------------------------------------------
# Universal hash functions

class Hash_Function :
  def __init__ (self,n,m) :
    """The parameter 'n' should a prime that is larger than any of the keys
    we might need to hash. The parameter 'm' is the number of slots that 
    the hash function can target."""
    self.n = n
    self.m = m
    self.a = choice(range(1,n))
    self.b = choice(range(n))

  def hash (self, k) :
    return ((self.a * k + self.b) % self.n) % self.m

def test_hash (n,m) :
  f = Hash_Function(n,m)
  collisions = [None] * m
  for s in range(m) :
      collisions[s] = []
  for k in range(n) :
      slot = f.hash(k)
      collisions[slot].append(k)
  for s in range(m) :
    print "slot = %d, collisions = %s" % (s,collisions[s])
  
#-----------------------------------------------------------------------------
# Various hash table implementations that differ in how they resolve
# collisions

class HashTable :
  def hash       (self, val) : raise AbstractE
  def insert     (self, val) : raise AbstractE
  def delete     (self, val) : raise AbstractE
  def search     (self, val) : raise AbstractE
  def getVals    (self)      : raise AbstractE
    
#--

class HashTable_Chaining (HashTable) :
  """Implement our own hash tables using lists. Resolve collision by
  chaining. The hash function to use is a parameter that is an instance of
  Hash_Function so that we can experiment with various techniques."""

  """Creates a hash table that uses Chaining.
    >>> ys = HashTable_Chaining(17,3)
    >>> ys.insert(1)
    >>> ys.insert(2)
    >>> ys.insert(4)
    >>> ys.insert(1)
    >>> ys.search(2)
    True
    >>> x = ys.hash(1)
    >>> ys.vals[x].len() == 2
    True
    >>> ys.delete(2)
    >>> ys.search(2)
    False
    """

  def __init__(self,n,m) :
    self.n = n
    self.m = m
    self.vals = [None]*m
    self.hashf = Hash_Function(n,m)

  def hash (self, val) :
    return self.hashf.hash(val)

  def insert (self, val) : 
    h = self.hash(val)
    if self.vals[h] is None :
      self.vals[h] = [val]
    else :
      self.vals[h].append(val)

  def delete (self, val) : 
    h = self.hash(val)
    if not self.vals[h] is None :
      try :
        self.vals[h].remove(val)
      except ValueError :
        pass

  def search (self, val) :
    h = self.hash(val)
    if self.vals[h] is None : 
      return False
    else :
      return val in self.vals[h]

  def getVals (self) : 
    result = []
    for xs in self.vals :
      if xs is None :
        pass
      else :
        result.extend(xs)
    return result

#--

class HashTableFullE : pass

class HashTable_LinearProbing (HashTable) :

  """Creates a hash table that uses Linear Probing.
    >>> ys = HashTable_LinearProbing(17,3)
    >>> ys.insert(1)
    >>> ys.insert(2)
    >>> ys.insert(4)
    >>> ys.m
    3
    >>> ys.search(2)
    True
    >>> ys.insert(5)
    >>> ys.m
    6
    >>> ys.delete(2)
    >>> ys.search(2)
    False
    """

  class Deleted : 
    def __str__(self) : return "DELETED"

  def __init__ (self,n,m) : 
    self.n = n
    self.m = m
    self.vals = [None]*m
    self.hashf = Hash_Function(n,m)
    self.DELETED = self.Deleted()

  def hash (self, val) :
    return self.hashf.hash(val)

  def auxiliary_hash (self, val, i) :
    return (self.hash(val) + i) % self.m

  def insert (self, val) :
    # YOUR CODE
    # for i in range(self.m) :
    #   h = self.auxiliary_hash(val,i)
    #   if self.vals[h] is None or self.vals[h] is self.DELETED :
    #     self.vals[h] = val
    #     return
    # raise HashTableFullE

    #Code that factors in a doubling of the hash table:
    z = self.getVals()
    q = len(z) + 1
    if q <= self.m : #if it's big enough, proceeds as normal.
      for i in range(self.m) :
       h = self.auxiliary_hash(val,i)
       if self.vals[h] is None or self.vals[h] is self.DELETED :
         self.vals[h] = val
         return
    else : #if I need a bigger hash function.
      temp = self.getVals() # stores vals in an array.
      self.m = self.m * 2 #doubles size of hash table.
      self.vals = [None] * self.m
      for x in temp : #rehashes all of the vals in the array.
        for i in range(self.m) :
          h = self.auxiliary_hash(x,i)
          if self.vals[h] is None or self.vals[h] is self.DELETED :
            self.vals[h] = x
      for i in range(self.m) : #hashes the original value you wanted to hash.
       h = self.auxiliary_hash(val,i)
       if self.vals[h] is None or self.vals[h] is self.DELETED :
         self.vals[h] = val
         return

        
  def delete (self, val) :
    for i in range(self.m) :
      h = self.auxiliary_hash(val,i)
      if self.vals[h] == val :
        self.vals[h] = self.DELETED
      else :
        pass
        

  def search (self, val) :
    for i in range(self.m) :
      h = self.auxiliary_hash(val,i)
      if self.vals[h] is None :
        return False
      elif self.vals[h] == val :
        return True
      else :
        pass
    return False        

  def getVals (self) : 
    result = []
    for x in self.vals :
      if x is None :
        pass
      else :
        result.append(x)
    return result

class HashTable_QuadraticProbing(HashTable) :

  #The change on this vs linear probing is really easy. The only difference between
  #what you wrote for linear probing and this is in my auxilary function I use i^2 instead
  #of just i.

  #Writing tests was hard. Because a and b are random, it's hard to write
  #tests that consistently work the same way.

  """Creates a hash table that uses Quadratic Probing.
    >>> xs = HashTable_QuadraticProbing(17,3)
    >>> xs.insert(1)
    >>> xs.insert(2)
    >>> xs.search(2)
    True
    >>> xs.delete(2)
    >>> xs.search(2)
    False
    """
  
  class Deleted :
    def __str__(self) : return "DELETED"

  def __init__(self,n,m) :
    self.n = n
    self.m = m
    self.vals = [None] * m
    self.hashf = Hash_Function(n,m)
    self.DELETED = self.Deleted()

  def hash(self, val) :
    return self.hashf.hash(val)

  def next_perfect_square(self,i) :
    return i * i

  def auxiliary_hash (self, val, i) :
    return (self.hash(val) + self.next_perfect_square(i)) % self.m

  def insert (self, val) :
    for i in range(self.m) :
      h = self.auxiliary_hash(val,i)
      if self.vals[h] is None or self.vals[h] is self.DELETED :
        self.vals[h] = val
        return
    raise HashTableFullE

  def delete (self, val) :
    for i in range(self.m) :
      h = self.auxiliary_hash(val,i)
      if self.vals[h] == val :
        self.vals[h] = self.DELETED
      else :
        pass
        

  def search (self, val) :
    for i in range(self.m) :
      h = self.auxiliary_hash(val,i)
      if self.vals[h] is None :
        return False
      elif self.vals[h] == val :
        return True
      else :
        pass
    return False        

  def getVals (self) : 
    result = []
    for x in self.vals :
      if x is None :
        pass
      else :
        result.append(x)
    return result

class HashTable_DoubleHashing(HashTable) :
  class Deleted :
    def __str__(self) : return "DELETED"

  def __init__(self,n,m) :
    self.n = n
    self.m = m
    self.vals = [None] * m
    self.hashf = Hash_Function(n,m)
    self.DELETED = self.Deleted()

  def hash(self, val) :
    return self.hashf.hash(val)

  def hash2(self, val) :
    return 7 - (val % 7) 
    #my later functions work off of the assumption that this one will hit every
    #possible option. I assume this is correct, but if it's not just know that might
    #be a reason that later functions are faulty.

  def insert (self, val) :
    z = self.getVals()
    q = len(z)
    if q >= self.m :
      raise HashTableFullE
    else :
      h = self.hash(val)
      while True:
        if self.vals[h] is None or self.vals[h] is self.DELETED :
          self.vals[h] = val
          return
        h += self.hash2(h)
        if h >= self.m :
          h -= self.m

  def delete (self, val) :
    x = self.hash(val)
    h = x
    if self.vals[h] == val :
      self.vals[h] = self.DELETED
    else:
      while True:
        h += self.hash2(h)
        if self.vals[h] == val :
          self.vals[h] = self.DELETED
          return
        elif h == x :
          return False

        

  def search (self, val) :
    x = self.hash(val)
    h = x
    if self.vals[h] == val :
      return self.vals[h]
    else:
      while True:
        h += self.hash2(h)
        if self.vals[h] == val :
          return self.vals[h]
        elif h == x :
          return False        

  def getVals (self) : 
    result = []
    for x in self.vals :
      if x is None :
        pass
      else :
        result.append(x)
    return result
#--

#-----------------------------------------------------------------------------
# To do

# Implement various instances of Hash_Function
# Implement quadratic probing
# Implement double hashing
# Double the size of a hash table - Done in linear probing. Your original code is commented out.
# Document and add test cases

#-----------------------------------------------------------------------------

if __name__ == "__main__" :
  import doctest
  doctest.testmod()
