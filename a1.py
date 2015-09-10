import math

def logStar(n):
  x = n
  while x >= 1:
    x = math.log(x, 2)
  return x

def nFactorial(n):
  x = n
  if x == 0:
    return 1
  else:
    while x > 1:
      n = n * (x-1)
      x -= 1
  return n

def groupOne(x) :
  print 'This is by far the fastest group: n = 5'
  print '1. 2^2^(n+1) is %f ' % \
    math.pow(2,math.pow(2,x+1))
  print '2. 2^2^n is %f' % \
    math.pow(2,math.pow(2,x))

def groupTwo(x) :
  print 'This is the second fastest group: n = 45'
  print '3. (n+1)! is %f' %\
    nFactorial(x+1) 
  print '4. n! is %f' % \
    nFactorial(x) 
  print '5. e^n is %f ' % \
    math.pow(math.e,x)
  print '6. n * 2^n is %f' % \
    (x * math.pow(2,x))
  print '7. 2^n is %f' % \
    math.pow(2,x)
  print '8. 1.5^n is %f' % \
    math.pow(1.5,x)
  print '9. lg(n!) is %f' % \
    math.log(nFactorial(x),2) 

def groupThree(x) :
  print 'This is the third fastest group: n = 2^32'
  print 'Tied 10. n^lglg is %f' % \
    math.pow(x,math.log(math.log(x, 2), 2)) # n = 2^32
  print 'Tied 10. lg^lg is %f' % \
    math.pow(math.log(x,2),math.log(x,2)) # n = 2^32
  print '11. lgn! is %f' %\
    nFactorial(math.log(x,2)) # n = 2^32
  print '12. n^3 is %f' % \
    math.pow(x,3) # n = 2^32
  print 'Tied 13. n^2 is %f' % \
    math.pow(x,2) # equal to 4^lg
  print 'Tied 13. 4^lg is %f' % \
    math.pow(4,math.log(x,2)) #equal to n^2
  print '14. nlg is %f' %\
    (x * math.log(x)) # n = 2^32
  print 'Tied 15. n is % f' % \
    x # equal to 2^lg
  print 'Tied 15. 2^lg is %f' % \
    math.pow(2,math.log(x, 2)) # = n

def groupFour(x) :
  print 'This is the slowest group: n = 2^64'
  print '16. sqrt(2)^lg is %f' % \
   math.pow(math.sqrt(2), math.log(x)) #2^64#
  print '17. (lgn)^2 is %f' % \
   math.pow(math.log(x,2),2) #2^64
  print '18. 2^sqrt(2lg) is %f' % \
   math.pow(2,math.sqrt(2 * math.log(x,2))) #2^64
  print '19. ln is %f' % \
   math.log(x,math.e) # 2^64
  print '20. sqrt(lg) is %f' %\
    math.sqrt(math.log(x,2))
  print '21. lnln is %f' % \
    math.log(math.log(x,math.e), math.e)
  print '22. n^(1/lg) is %f' % \
    math.pow(x, 1/math.log(x))
  print '23. 2^lg* is %f' % \
    math.pow(2, logStar(x))
  print '24. 1 is 1, no computation needed here.'
  print 'Tied 25. lg* is %f' % \
    logStar(x) # same as lg*lg
  print 'Tied 25. lg*lg is %f' % \
    logStar(math.log(x,2)) # same as lg*
  print 'And last but not least our slowest growing function! Yes, it is still negative at 2^64'
  print '26. lglg* is %f' % \
    math.log(logStar(x),2)

if __name__ == "__main__" :
  
  groupOne(5)
  groupTwo(45)
  groupThree(math.pow(2,32))
  groupFour(math.pow(2,64))



