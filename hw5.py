#################
# Name: Biken Maharjan
# Course: Cs235
# HW: 0101  
#################


from math import floor
from fractions import gcd
from random import randint
from urllib.request import urlopen

'''
#1
a.[3, 5, 4, 0, 1, 2] o [4, 5, 3, 1, 2, 0]
  = [1, 2, 0, 5, 4, 3]

b. [441,442,...,999,0,1,2,3,4,...,440] o [176,177,...,999,0,1,2,3,4,...,175] = ?
  = 441 + 1000Z  && 176 + 1000Z
  = (617) + 1000Z
  = [617, 618, ........,999,0,1,2,3,....,615,616]

c. p o p o [4,5,6,0,1,2,3]
   p o [4,5,6,0,1,2,3] - > [4,5,6,0,1,2,3]
   p o ( p o [4,5,6,0,1,2,3] ) ->[4,5,6,0,1,2,3]

d. q^-1 o p^-1 o q^-1 o q o p o q
    p = [0,1,2,3,4]
    q = [4,0,1,2,3]
                     <------------
    q^-1 o p^-1 o q^-1 o q o p o q
    
    p o q = [4,0,1,2,3]
    q o p o q = [3,4,0,1,2]
    q^-1 o q o p o q = [3,2,1,0,4]
    p^-1 o q^-1 o q o p o q = [4,0,1,2,3]
    q^-1 o p^-1 o q^-1 o q o p o q = [3,2,1,0,4] = q^-1
    
e.   
    (Z/4Z)* = [1,3]
    [0,1] -> 0 & [1,0] ->1

    [0,1] o [0,1] = [0,1]     |   1 . 1 = 1 
    [0,1] o [1,0] = [1,0]     |   1 . 3 = 3
    [1,0] o [0,1] = [1,0]     |   3 . 1 = 3
    [1,0] o [1,0] = [0,1]     !   3 . 3 = 1

f. 


g. Different cardinality. Doesn't follow homomorphism because of it, no isomorphism occur.
   In order to be an isomorphism, initial criteria require is to have same number of element.    

'''
    

#///////////////////////////////////////////////////////////////////////////////////////////////
#A

def permute(p,l):
    ls = []
    for i in range(0,len(p)):
        ls.append(l[p[i]])
    return ls     

def C(k , m):
    ls = []
    for i in range(0,m):
        ls.append((i+k) % m)
    return ls

def M(a, m):
    ls = []
    for i in range(0,m):
        ls.append((a * i) % m)
    return ls

def sortCheck(ls):
    l = list(ls)
    l.sort()
    if l == ls :
        return True
    else:
        return False
    
def sort(l):
    for x in range(1,len(l)):
                            #cyclic
        cp  = C(x,len(l))
        cyc = permute(cp,l)
       
        #T then return:
        if sortCheck(cyc):
            return cp
        #return cp

                            #multiplication-induced permutation
        mp = M(x,len(l))
        mulP = permute(mp,l)

                            #True then return:
        if sortCheck(mulP):
            return mp
                            #return mP

    return None 
    
#///////////////////////////////////////////////////////////////////////////////////////////////
#########
# @Provided Code for previous Assignment 
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
      return None         # then return none  
   (s,t) = egcd(a,m)
   return s % m
#///////////////////////////////////////////////////////////////////////////////////////////////
def unreliableUntrustedProduct(xs, n):
    url = 'http://cs-people.bu.edu/lapets/235/unreliable.php'
    return int(urlopen(url+"?n="+str(n)+"&data="+",".join([str(x) for x in xs])).read().decode())
#Following RSA

def privateProduct(xs, p, q):
    n = p * q
    phi = (p-1)*(q-1)
    e = phi - 1
    
    inverse = inv(e,phi)
    c = [pow(xs[i],e,n) for i in range(0,len(xs))] #encrytion data
    ans = unreliableUntrustedProduct(c, n)         #passed to unreliable server
    return pow(ans,inverse,n)                      #returns decrypts the answer that was send by server  

#########
# a function solveOne(c, b, a, m) that takes four integers c, b, a,
# and m ≥ 1. If c and m are coprime, the function returns the solution x ∈ {0, ..., m-1}
#########
def solveOne(c,b,a,m):
   if gcd(c,m) == 1 :
       return ((a-b) * inv(c,m)) % m
   return None

                                           #RSA protocol to ecrypt and decrpyt
def validPrivateProduct(xs,p,q):
    r = randint(0,q)                       # create random number in a range of (0 to q)
    n = p*q                                # create key [public]
    phi_n = (p-1) * (q-1)                  
    e = 0
    for i in range(2,phi_n-1):
        if gcd(i,phi_n) == 1:                #no Common factor then go ahead                
            e = i
            break                            # find inverse 
        d = inv(e,phi_n)                     #similar to above func but this time, we are looping multiple time
        for i in range(0,len(xs)):       
            xs[i] = (xs[i] * q * inv(q,p) + r * p * inv(p,q))
            product = unreliableUntrustedProduct(xs, n)
        while (product % q) != pow(r,len(xs),q):     
            validPrivateProduct(xs,p,q)
        return (product % p)
#[rm]
#########
# a function solveTwo(e1,e2) takes in e1 and e2 tuples and returns the solution x ∈ {0, ..., m-1}
#########

def solveTwo(e1,e2):
    if gcd(e1[0],e1[3]) != 1 or gcd(e2[0],e2[3]) != 1 :  # check whether any of (c,m) are not co-prime
         return None                                    # if so return 'None' string literal 
    a = solveOne(e1[0],e1[1],e1[2],e1[3])           # accesing tuples (c,b,a,m) and passing it as arguement in solveOne Func
    b = solveOne(e2[0],e2[1],e2[2],e2[3])           #  'ditto'
                                                    # applying chinese remainder theorem
            # form of -> ( (a* m2* (inverse of m2) ) + b* m1* (inverse of m1) ) % (m1*m2)                                          
    return ((a*e2[3]*inv(e2[3],e1[3])) + (b*e1[3]*inv(e1[3],e2[3]))) % (e1[3]*e2[3])

#///////////////////////////////////////////////////////////////////////////////////////////////

#change [done]
#comment []
def isomorphism(A,B):
    
    c = [None] * len(A[0])
    
    for i in range(0,len(A[0])):
        c[i] = (A[0][i],B[0][i])
    d = [None] * len(A[0])
    
    for i in range(0,len(d)):
        for z in range(i+1,len(d)):
            d[i] = ( A[1]( c[i][0], c[z][0]) ,B[1]( c[i][1] , c[z][1]) )
            
    for i in range(0,len(d)):
        e = c.pop()
        if type(e[1]) == list:
            if (e in d == False or e[1][0] in d == False):
                return False
        elif (e in d) == False:
            return False 
    return True
#///////////////////////////////////////////////////////////////////////////////////////////////
#[Extra_credit]
'''
a.
  ((z/8z)*,.)     ((z/10z)*,.)

  * 1 3 5 7        * 1 3 7 9
  ---------        --------- 
  1|1 3 5 7        1|1 3 7 9
  3|3 1 7 5        3|3 9 1 7
  5|5 7 1 3        7|7 1 9 3
  7|7 5 3 1        9|9 7 3 1

  Even though both  ((z/8z)*,.) and ((z/10z)*,.) have same size phi(8) == phi(10) but their multiplication
  table is different. In ((z/8z)*,.) table, identity element is form whenever two similiar number is multiplied.
  # * # = e [identity] but in ((z/10z)*,.) we don't use such occurance. Hence, these are not isomorphic. They are not
  identical.


b. (z/4z,+)        ((z/8z)*,.)

   + 0 1 2 3       * 1 3 5 7
   ---------       ---------  
   0|0 1 2 3       1|1 3 5 7  
   1|1 2 3 0       3|3 1 7 5
   2|2 3 0 1       5|5 7 1 3
   3|3 0 1 2       7|7 5 3 1

   [similar to above ]
   These two are not isomorphic. Since their multiplication table is not identical.
   
'''



    
    
