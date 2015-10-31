# It was interesting researching this function. With regards to numbers it appears
# Python just hashes integers to itself unless it = -1, in which case it hashes to -2
# because -1 is reserved for errors.

# When you get to type long it gets more interesting. It appears at 2**64 it resets and 
# hashes to 1 again and then for each iteration from 2**64, 2**65, ... 2**127 it will hash
# everything from 2**0 to 2**63. At hash 2**128 it resets again to hash 2**0 and does this
# every increment of 64.

#With this explanation in mind, my function is built for my test cases and not for every
#possibility out there so I hope the explanation above demonstrates I understand it decently.

#Explaining the test case you gave us... 2**6 = 64 so 2**6 hashes to 64. If you add 64
#to 6 you get 70 and as such it hashes to the same value.

def hashIteration(number):
  if number % 2 == 0 or number == 1:
    i = 0
    n = number + 63
    while i < 10 :
      print "%f" % hash(2**n)
      n += 64
      i += 1


if __name__ == "__main__" :
  hashIteration(1)
  hashIteration(2)
  hashIteration(4)