#####Session1
# print("Welcome to python")

# #####Session2

# n1=10
# n2=20
# add=n1+n2
# print(add)

# Variable name should start with lower case char
# Digits are allowed but not at the start
# "_"Underscore is allowed

#functions-1)id  2)type
# print(type(n1),type(n2))
# print(id(n1),id(n2))

#Object Intering
# object intering--if two variable have same value then python creat a single object for those variables
# here we will see memory allocation is same for same value it is called object intering
# a=10
# b=10
# print(id(a),id(b))

#####Session3
#Data Types---

#int
# n1=100
# print(type(n1))

#float
# n1=23.34
# print(type(n1))

#int and float are immutable(not changed) data
# n1=100
# print(id(n1))
# n1=105
# print(id(n1))
# when we run both values store in different memory location

# str in ' ', " ", """ """
# it is immutable 
# s="'python' sample"
# print(id(s))
# print(s,type(s))

#list[]--mutable data type
# l=[1,2,3,4,5,"py",'DJ']
# l.append(6)  #TO Add another value in list we use append
# print(l)

# Tuple--immutable data type
# t=(1,2,3,4,5)  #approx same as a list

# Dict--mutable data type
# d={"name":"abc","email":adf@gmail.com}

# set--mutable data type
# s={1,2,3,4,5}

# bool:True False

# complex: 4+3j

#Operaters--

#Arithmetic operater +,-,*,/,//,%,**
# n1=3
# n2=5
# print(n1+n2)
# print(n1-n2)
# print(n1*n2)
# print(n1/n2)
# print(10/3)   #give float ans
# print(10//3)   #give int ans
# print(10%3)
# print(10**3)

#comparision operators  <,>,<=,>=,==,!=
# n1=100
# n2=45  #n2=100, it give True
# print(n1==n2)
# # these operators give ans in True or False

#identity opertors
# n1=100
# n2=100
# print(n1==n2)
# print(n1 is n2)

# l=[1,2,3]
# l1=[1,2,3]      #is compare memory allocatio
# print(l==l1)
# print(l is l1)
# print(l is not l1)

#Assinment Operators =,+=,-=,*=,/=
# n1=34
# n1/=5
# print(n1)

#Bitwise Operators &,|,^,>>,<<
# n1=2
# n2=1
# print(bin(n1),bin(n2))  #bin use to convert in binary

#Logical Operators  and, or, not
# print(10==11 and 20==20)
# print(10==10 and 20==20)
# print(10==10 or 20==67)
# print(not(10==10))
# print(not(10==14))

#Membership Operators in, not in
# l=[1,2,3,4,5]
# print(3 in l)
# print(45 in l)
# s="python str"
# print("python" in s)
# print("python"not in s)
