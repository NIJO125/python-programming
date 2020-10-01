#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import fractions 
def tocalc():
    sum=1
    for i in range(1,11):
      sum *= i // fractions.gcd(i,sum)
    return sum
if __name__=="__main__":
  print(tocalc())

