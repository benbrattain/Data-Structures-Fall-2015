
# Python idioms

def prod (xs) :
  result = 1
  for x in xs : 
    result = result * x
  return result

def prod1 (xs) :
  return reduce (lambda a , b : a * b, xs, 1)

def evens1 (xs) :
  return filter(lambda x : x % 2 == 0, xs)

def evens2 (xs) :
  return [ x for x in xs if x % 2 == 0 ]

# Stack size

def even (i) :
  if i == 0 : 
    return True
  else :
    return odd(i-1)

def odd (i) :
  if i == 0 : 
    return False
  else :
    return even (i-1)

# In my python implementation:
# even(998) works
# even(999) blows the stack

# Heap allocation

def mod (xs) : 
  xs[0] = 3
  return xs

def usemod () :
  xs = range(10)
  ys = mod(xs)
  return xs == ys

def outer () :
  xs = range(10)
  def inner (ys) :
    return xs == ys
  return inner(xs)

# Closures

def escape (i) :
  j = i+1
  k = j*2
  return (lambda x : x + i + j + k)

def use (i) :
  j = i*100
  k = j-23
  return escape(i+5)(i)

# Closures are special objects with one method only

# Interpreter pattern for defining data structures with several
# variants. For a class list, we would have two subclasses one for the
# empty list case and the non-empty list case. 

# First a few exceptions classes

class EmptyListE :
  def __repr__(self) :
    return "Exception: list is empty"

class NotFoundE :
  def __repr__(self) :
    return "Exception: element not found"

class IndexOutOfBoundsE :
  def __repr__(self) :
    return "Exception: index out of bounds"

# The parent class: only one method works generically on empty and
# non-empty lists

class List :

  def add(self,v) :
    return Node(v,self)

# Methods specific to empty lists

class EmptyList (List) :

  def size (self) :
    return 0

  def isEmpty (self) :
    return True

  def search (self, v) :
    return False

  def elem (self, i) :
    raise IndexOutOfBoundsE()

  def index (self, v) :
    raise NotFoundE()

  def insert(self, i, v) :
    if i == 0 :
        return Node(v,self)
    else :
        raise IndexOutOfBoundsE()

  def remove(self,v) :
    return self

  def append(self,v) :
    return Node(v,self)

  def drop(self,i) :
    if i == 0 :
     return self
    else : 
      raise IndexOutOfBoundsE()

  def __repr__ (self) :
    return "[]"

# Methods specific to non-empty lists

class Node (List) :

  def __init__ (self, head, tail) :
    self.head = head
    self.tail = tail

  def size (self) :
    return 1 + self.tail.size()

  def isEmpty (self) :
    return False

  def search (self, v) :
    return self.head == v or self.tail.search(v)

  def elem (self, i) :
    if i == 0 :
        return self.head
    else :
        return self.tail.elem(i-1)

  def index (self, v) :
    if self.head == v :
        return 0
    else :
        return 1 + self.tail.index(v)

  def insert(self, i, v) :
    if i == 0 :
        return Node(v,self)
    else :
        return Node(self.head,self.tail.insert(i-1,v))

  def remove(self,v) :
    if self.head == v :
        return self.tail
    else :
        return Node(self.head,self.tail.remove(v))

  def append(self,v) :
    return Node(self.head,self.tail.append(v))

  def drop (self,i) : 
   if i == 0 :
       return self
   else :
       return self.tail.drop(i-1)

  def __repr__ (self) :
    return "%s, %s" % (self.head, self.tail)

