'''
* Assignment #1
* Name: Biken Maharjan
* Course:CS235
* ----------------------
* Assignment 1
* filename: hw1.py
'''
#Decleration for seperator functioemptySet={}

def forall(X, P):
    S = {x for x in X if  P(x)}
    return len(S) == len(X)

def perfectSquares(n):
     return {(x*x) for x in range(1,n+1) if x*x <= n}
    
def squareFree(n):
    return  forall(perfect_square_no_one(n), lambda k: ((n%k != 0)))

def perfect_square_no_one(n):
    return {(x*x) for x in range(2,n+1) if x*x <= n}

def same(n,m):
    new_n = forall(perfect_square_no_one(n), lambda k: ((n%k != 0)) )  #This part as well
    new_m = forall(perfect_square_no_one(m), lambda k: ((m%k != 0)) )  
    return new_n == new_m

def seperator(emptySet):
    return{(x,y) for x in emptySet for y in emptySet if same(x,y)}

#notReflexiveOn  = none
notSymmetricOn  = {1,4}   # symmetric is conditional
notTransitiveOn = {1,2,4}
#===========================================================================================================================
def subset(X,Y):
  return forall(X, lambda x: x in Y)

def product(X, Y):
  return { (x,y) for x in X for y in Y }

def relation(R, X):
  return R.issubset(product(X, X))

def isReflexive(m,n): 
    return relation(n,m) and forall(m, lambda x: (x,x) in n)

def isSymmetric(m,n):  
    return relation(n,m) and forall(m, lambda x: forall(m,lambda y: ((x,y) in n) <= ((y,x) in n)))

def isTransitive(m,n):
    return relation(n,m) and forall(m, lambda x: forall(m,lambda y: forall(m,lambda z:(((x,y) in n) and ((y,z) in n) ) <= ((x,z) in n))))

def isEquivalence(m,n):
    return isReflexive(m,n) and isSymmetric(m,n) and isTransitive(m,n)

#===========================================================================================================================
def quotient(X,R):
    return{frozenset({y for y in X if (x,y) in R}) for x in X}

def quotient_flight(X,R):
     mylist= {frozenset({y for y in X if (x,y) in R }) for x in X}
     mylist.remove(max(mylist,key=len))
     return mylist

def quotient_drive(X,R):
     mylist= {frozenset({y for y in X if (x,y) in R }) for x in X}
     return max(mylist,key=len)


X1 = {"a","b","c","d","e","f"}
R1 = {("a","a"),("b","b"),("c","c"),("d","d"),("e","e"),("f","f"),("a","c"),("c","a"),("b","d"),("d","b"),("e","f"),("f","e")}

X2 = {0,1,2,3,4,5,6,7,8,9,10,11}
R2 = {(0,2),(2,4),(4,0),(6,2),(6,0),(6,4),(8,4),(8,0),(8,6),(8,2),(10,6),(10,8),(10,4),(10,0),(10,2),(0,0),(2,2),(4,4),(6,6),(8,8),(10,10),(1,3),(5,3),(5,1),\
      (7,5),(7,3),(7,1),(9,7),(9,5),(9,3),(9,1),(11,9),(11,7),(11,7),(11,5),(11,3),(11,1),(1,1),(3,3),(5,5),(7,7),(9,9),(11,11),(3,1),(3,5),(1,5),(5,7),(3,7),\
      (1,7),(7,9),(5,9),(3,9),(1,9),(9,11),(7,11),(5,11),(3,11),(1,11),(2,0),(4,2),(0,4),(2,6),(0,6),(4,6),(4,8),(0,8),(6,8),(2,8),(6,10),(8,10),(4,10),(0,10),\
      (2,10)}
X3 = set(range(0,90))
R3 = 0 #
#===========================================================================================================================

C = {'Iceland','Vietnam','Kazakhstan','Australia'}

#relation is being able to drive 
# addition info without actually changing any relation in D
D = {('Vietnam', 'Kazakhstan'), ('Kazakhstan', 'Vietnam'),('Australia','Australia'), ('Iceland','Iceland'),('Vietnam','Vietnam'),('Kazakhstan','Kazakhstan')}

#Quotient set that doesn't have any connection to other city is the require number.
def minimumFlights(C,D):
    return len(quotient_flight(C,D));

# longest quotient set is the longest drive here.
def longestDrive(C,D):
    return len(quotient_drive(C,D))
#===========================================================================================================================

    


