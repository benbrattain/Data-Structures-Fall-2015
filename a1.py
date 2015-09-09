import math
from matplotlib.pyplot import plot, show, subplot, text, title
from inspect import getsource
# import code;

def logStar(n):
  x = n
  while x >= 1:
    x = math.log(x, 2)
  return x

def nFactorial(n):
  x = n
  while x > 1:
    n = n * (x-1)
    x -= 1
  return n


if __name__ == "__main__" :
  def runThis(x) :
    # print '(n+1)! is %f' %\
      # nFactorial(x+1) # n = 100
    # print 'n! is %f' % \
      # nFactorial(x) # n = 100
    # print 'lg(n!) is %f' % \
      # math.log(nFactorial(x),2) # n = 100
    # print 'n^lglg is %f' % \
    #   math.pow(x,math.log(math.log(x, 2), 2)) # n = 2^32
    # print 'lg^lg is %f' % \
    #   math.pow(math.log(x,2),math.log(x,2)) # n = 2^32
    # print 'lgn! is %f' %\
    #   nFactorial(math.log(x,2)) # n = 2^32
    print 'lglg* is %f' % \
      math.log(logStar(x),2)
    print '2^lg* is %f' % \
      math.pow(2, logStar(x))
    print 'sqrt(2)^lg is %f' % \
      math.pow(math.sqrt(2), math.log(x))
    print 'n^2 is %f' % \
      math.pow(x,2)
    print 'n^3 is %f' % \
      math.pow(x,3)
    print '(lgn)^2 is %f' % \
      math.pow(math.log(x,2),2)
    print 'n^(1/lg) is %f' % \
      math.pow(x, 1/math.log(x))
    print 'lnln is %f' % \
      math.log(math.log(x,math.e), math.e)
    print 'lg* is %f' % \
      logStar(x)
    print 'ln is %f' % \
      math.log(x,math.e)
    print '2^lg is %f' % \
      math.pow(2,math.log(x, 2))
    print '4^lg is %f' % \
      math.pow(4,math.log(x,2))
    print 'sqrt(lg) is %f' %\
      math.sqrt(math.log(x,2))
    print 'lg*lg is %f' % \
      logStar(math.log(x,2))
    print '2^sqrt(2lg) is %f' % \
      math.pow(2,math.sqrt(2 * math.log(x,2)))
    print 'n is % f' % \
      x
    print 'nlg is %f' %\
      (x * math.log(x))



  runThis(100.00)


