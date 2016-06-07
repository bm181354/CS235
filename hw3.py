'''
# Name: Biken Maharjan
# =====================
# Course : CS235
# Topics : Fermat's Little theorem, Euler's Theorem, CRT
# Assignment # 0 0 1 1
'''

#########
# Allowed Standard Library
#########

from math import floor
from fractions import gcd


'''
#1
 1.a
  5 * x ≡ 3 (mod 11)
  5 * x ≡ 25 
  5 * x ≡ 5 * 5     [remove 5 on both side using Euclid's lemma]
      x ≡ 5 (mod 11)
  1.b
   8 * x − 1 ≡ 1 (mod 5)
   8 * x − 1 + 1 ≡ 1 + 1
   8 * x  ≡ 2 
   8 * x  ≡ 32 
   8 * x  ≡ 8 * 4   [remove 8 on both side using Euclid's lemma]
       x  ≡ 4 (mod 5)
////
  1.c
   x ≡ 4 (mod 7)
   x ≡ 3 (mod 5)
    x ≡ a * m2 *(inverse of m2)+ b * m1 * (inverse of m1)  
    x ≡ 4 * 5 * (inverse of 5) + 3 * 7 * (inverse of 7) ---[main equation]

     Finding inverse of 5:
       5^(7-1) ≡ 1 (mod 7) 
       5 * 5^(7-2) ≡ 1 (mod 7)
       5 * 3 ≡ 1(mod 7) --[ inverse is 3 ]
       
     Finding inverse of 7:
       7^(5-1) ≡ 1 (mod 5) 
       7 * 7^(5-2) ≡ 1 (mod 5)
       7 * 3 ≡ 1(mod 5) --[ inverse is 3 ]

     Replacing inverses in main equation:
       x ≡ (4 * 5 * 3 + 3 * 7 * 3) mod (7 * 5)
       x ≡ (18) mod (35)  [Ans]
/////
  1.d
   x ≡ 3 (mod 5)
   x ≡ 6 (mod 14)
 
    x ≡ 3 * 14 * (inverse of 14) + 6* 5 * (inverse of 5) ---[main equation]

    Finding inverse of 14:
        14*14^(5-2) ≡ 1 (mod 5)
        inverse of 14 is [4]  
        
       
     Finding inverse of 5:
        5 * 5^(14-2) ≡ 1 (mod 14)
        inverse of 5 is [3]

     Replacing inverses in main equation:
        x ≡ 3 * 14 * 4 + 6* 5 * 3 (mod 5 * 14)
        x ≡ 48 (mod 70) [Ans]
/////
  1.e
   x ≡ 10 (mod 11)
   3 * x ≡ 1 (mod 4)
    => 3 * x ≡ 3 * 3 (mod 4)
           x ≡ 3 (mod 4)
   x ≡ 3 (mod 4)          
 
   x ≡ 10 * 4 * (inverse of 4) + 3* 11 * (inverse of 11) ---[main equation]
    
   Finding inverse of 4:
        4*4^(11-2) ≡ 1 (mod 11)
        inverse of 4 is [3]

   Finding inverse of 11:
        11*11^(4-2) ≡ 1 (mod 4)
        inverse of 11 is [7]

   Replacing inverses in main equation:
        x ≡ 10 * 4 * 3 + 3* 11 * 7 (mod 44)
        x ≡ 43 mod(44) [Ans]
/////
   1.f
     q ⋅ x ≡ 3 (mod p)
         x ≡ 2 (mod q)

         x ≡ 3 * q^(-1) * q * q^(-1)   --- [i]
         x ≡ 2 * p * p^(-1)   --- [ii]
         
   Replacing inverses in main equation:
         x ≡ 3 * 4 * 4 * q + 2 * p * 5
         x ≡ (48 q + 10 p) mod (p * q)
         
'''
#//////////////////////////////////////////////////////////////////////////////////////////

#########
# Function returns the multiplicative inverse
# of a ∈ ℤ/pℤ (if a ≡ 0, it returns None)
# Assumption all the numbers are prime.
#########

def invPrime(a,p):
     if a == 0 :
         return None
     return pow(a,p-2,p)
#########
# @Provided Code for Assignment 
#########

def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
    return (s, t)
#########
#  Func returns the multiplicative inverse of a ∈ ℤ/mℤ.
#  If a and m are not coprime, it returns None
#########

def inv(a,m):
   if gcd(a,m) != 1:      # if m is not the co-prime of a
      return None       # then return none  
   (s,t) = egcd(a,m)
   return s % m
#########
# a function solveOne(c, b, a, m) that takes four integers c, b, a,
# and m ≥ 1. If c and m are coprime, the function returns the solution x ∈ {0, ..., m-1}
#########

def solveOne(c,b,a,m):
   if gcd(c,m) == 1 :
       return ((a-b) * inv(c,m)) % m
   return None
#########
# a function solveTwo(e1,e2) takes in e1 and e2 tuples and returns the solution x ∈ {0, ..., m-1}
#########

def solveTwo(e1,e2):
    if gcd(e1[0],e1[3]) != 1 or gcd(e2[0],e2[3]) != 1 :  # check whether any of (c,m) are not co-prime
         return None                                   # if so return 'None' string literal 
    a = solveOne(e1[0],e1[1],e1[2],e1[3])           # accesing tuples (c,b,a,m) and passing it as arguement in solveOne Func
    b = solveOne(e2[0],e2[1],e2[2],e2[3])           #  'ditto'
                                                    # applying chinese remainder theorem
            # form of -> ( (a* m2* (inverse of m2) ) + b* m1* (inverse of m1) ) % (m1*m2)                                          
    return ((a*e2[3]*inv(e2[3],e1[3])) + (b*e1[3]*inv(e1[3],e2[3]))) % (e1[3]*e2[3])
#########
# The function solveAll() should return the unique congruence class solution x to the above system of equations
# retuns -> a list 
#########

def solveAll(es):

    while es:                                       # iterate until list:[es] is null 
       e1 = es.pop()                                # Retrieve an arbitrary element from the set and remove it
       e2 = es.pop()                                # another arbitrary element from the set and purge it
       x = solveTwo(e1,e2)                          # also checks for co-prime from previous/above implementation and  
                                                    # returns -> 'None' for any unsolvable problem 
       # checking for the iterator control
       if not (es):                                 # after popping checking whether list is empty or not
           return x                                 # if empty then return x as the answer 
       # if set is not empty then send our newly
       # found equation into the list
       equation = (1,0,x,e1[3]*e2[3])                # tuple (a,b,c,m) -> c * x + b ≡ a (mod m)
       es.append(equation)                            
    return None
#########
# function sumPowsModPrime(nes, p) that takes a list nes representing a sum of powers and, as efficiently as possible,
# computes the sum modulo a prime p. 
# normally it could freeze the IDE if done in a traditional way 
#########

def sumPowsModPrime(ns,p):
     
     result = (sum( [pow(n, e % (p-1), p) for (n, e) in ns])) % p  # (n,e) <- n is the base and e is the exponent
     
     return (result)     
#########
# a function sumPowsModPrimes(nes, ps) that takes a list of one or more tuples nes as its first argument,
# and a list of one or more primes ps as its second argument and returns -> sum of powers as its output 
#########

def sumPowsModPrimes(nes, ps):
    container = []
    
    for p in ps:
        container = container + [(1, 0, sum([pow(n, e % (p-1), p) for (n, e) in nes]), p)]
        
    return solveAll(container)

#//////////////////////////////////////////////////////////////////////////////////////////
#****************************[EXTRA-CREDIT]************************************************
#########
# Allowed Standard Library for Extra credit
#########
from random import randint

################
# Function that takes in an +ve integer as an argument (m),
# returns boolean true for (T/F positive) probable prime and composite as (true negative) boolean false
# Algorithm (Fermat primality test)
################
def probablePrime(m):
    k = 35                                  #  k ∈ ℕ, 
    for i in range(2,k):                    
        a = randint(2,m)      # generate random number between [2,m-1]  
        #print(a)
        #print(m)
        if (m % a) == 0:  return False
        if gcd(a,m) != 1: return False
        if pow(a,m-1,m) != 1: return False  # time complexity of O(n) faster than a^(m-1)%m which is 0(n^2)
        #print(a)
    return True

################
# Function that takes in an +ve integer as an argument (n),
# returns a list of k prime numbers corresponding to the users' nth digit desire.   
################

def makePrime(d,k):                                   # assuming d > = 1 
    primeContainer = [] 
    nthSNum = pow(10,(d-1))                         # the smallest nth digit number
    nthBNum = pow(10,d) - 1                         # the biggest nth digit number
    p = randint(nthSNum,nthBNum)             # any possible number + nthSNum = nth digit number in any case
    #print(p)
    while k > len(primeContainer):          # loop arounds until length of list is [k-1]
         while not probablePrime(p):        # loops until it finds a prime [P]
           p = randint(nthSNum,nthBNum)     # p is assigned with the random value having nth-digit place number.
           
         if p not in primeContainer:        # checks whether [p] exists in list or not; to negate duplication             
           primeContainer.append(p)         # then appends the number into the list, also used for iteration control
    return primeContainer 

       

       

       

  
















