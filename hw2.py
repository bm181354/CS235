#Assignment #2

'''
*Name: Biken Maharjan
*========================
*Course : CS235
*Topics : Euclid's lemma, Random Number Generator Algorithm, GCD, Prime Generator
'''

#########
# Allowed Standard Library
#########

from fractions import gcd
from math import log

#1 
'''
#a
4*x +1 ≡ 9(mod 17)
4*x + 1 -1 ≡ 8  [addition and subtraction are relatively similar in modulo arithematic as regular arithematic]
4*x ≡ 4*2       [4 and 17 are co-prime, we can use Euclid's lemma]
x ≡ 2           [using Eculid's Lemma]

#b
5*x +2 ≡ -6 (mod 11)
5*x + 2 - 2 ≡ -8
5*x ≡ 5*5   [5 and 11 are co-prime, we can use Euclid's lemma] 
x ≡ 5       [using Eculid's Lemma]

#c
10*x -2 ≡ 3(mod 5)
10*x -2 +2 ≡ 5
10*x ≡ 10 * 2  [5 and 10 have factors in common, we can't use Euclid's lemma]
#error #No sol
 

#d
17*x +44 ≡ 333(mod 389)
17*x +44 -44 ≡ 333 - 44
17*x ≡ 289 
17 * x ≡ 17 * 17    [using Eculid's Lemma]
x  ≡  17            [17 and 389 are co-prime,using Euclid's lemma remove 14 from L.H.S and R.H.S]

#e
16 * x + 1 ≡ 3 (mod 8)
16*x + 1 - 1 ≡ 2
16*x ≡ 2
s#doesn't support Euclid's lemma to proceed with "cancellation" of any side


#f
5*x + 7 ≡ 13(mod 29)
5*x +7 -7 ≡ 13-7
5*x ≡ 6 
5 * x ≡ 5 * 7    [using Eculid's Lemma]
x  ≡  7

#g
11*x +5x ≡ 64(mod 587)
11*x +5x ≡ 64
16*x ≡ 16 * 4 
x ≡ 4    [using Eculid's Lemma]

#h
146467848 * x ≡ 43698243047256 (mod 7777777777777777777777777)
146467848 * x ≡ 146467848 * 298347     [using Eculid's Lemma]
x ≡ 298347

#i
650472472230302 * x ≡ 1 (mod 8910581811374)
650472472230302 * x ≡ 8910581811375 
#error, doesn't follow Euclid's lemma
 

'''
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
################
# Function that takes in an integer and list as an argument,
# returns number closest with the key.
################

def closest(key, xs): 
    low = xs[0]                             # lowest diff assigned to the 1st key
    for x in xs :

      if ( abs(key - x) < abs(key - low) ): # conditional to check which absolute value is the smallest
               low = x                      # assign x as the smallest diff
    return low

################
# Function that takes in an +ve integer as an argument (m),
# returns an integer b where b > 1 and b is coprime with m
################
  
def findCoprime(m):
    p = (2 * m // 5) + 3                    #Any arbitrary number in {3,...,m-1} #change
   # print(p)
    while gcd( p - 1 , m) != 1:             #While p − 1 and m are not coprime
#       print(p)
#       print(m)
       p = p * gcd(p - 1, m)
    return p - 1

################
# Function that takes in an +ve integer as an argument (m),
# returns an integer random number corresponding to a index.
# +Adv: doesn't hold any extra stack memory compare to STL rand generator
################

def randByIndex(m,i):
    a = findCoprime(m)
    
    a = (( (a * i)) % m )
    #print(a)   #2
    return a

################
# Function that takes in an +ve integer as an argument (m),
# returns boolean true for (T/F positive) probable prime and composite as (true negative) boolean false
# Algorithm (Fermat primality test)
################
def probablePrime(m):
    k = 35                                  #  k ∈ ℕ, 
    for i in range(2,k):                    
        a = randByIndex((m)-2,i) + 2      # generate random number between [2,m-1]  
        #print(a)
        #print(m)
        if (m % a) == 0:  return False
        if gcd(a,m) != 1: return False
        if pow(a,m-1,m) != 1: return False  # time complexity of O(n) faster than a^(m-1)%m which is 0(n^2)
        #print(a)
    return True

################
# Function that takes in an +ve integer as an argument (n),
# returns a prime number corresponding to the users' nth digit desire.   
################

def makePrime(d):                                   # assuming d >= 1  
    index = 1
    nthSNum = pow(10,(d-1))                         # the smallest nth digit number
    nthBNum = pow(10,d) - 1                         # the biggest nth digit number
    p = randByIndex(nthBNum - nthSNum,index) + nthSNum  # any possible number + nthSNum = nth digit number in any case
    #print(p)
    while not probablePrime(p):
          index = index + 1
          p = randByIndex(nthBNum - nthSNum,index) + nthSNum  #  p is assigned with the random value having nth-digit place number.
    return p    
    

    

        
    




