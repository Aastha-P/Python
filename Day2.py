######Session1
# Conditional statement
# if [Condition]:
# 	statement
# elif [Condition]:
# 	statement
# else:
#     statement

# n1=700
# n2=500
# if n1>n2:
#     print("n1 is greater than n2")    	
# elif n2>n1:
# 	print("n2 is greater than n1")
# else:
#     print("both are equal")	

# if 0 : # if we take 1 in place of 0 it gives True
# 	print("if block")
# else:
#     print("else block")	



#######Session2
# #loops--for,while
# #for loop
# # for [variable name] in [iterable datatype]:
# # 	  statements
# #Iterable datatype--str,list,tuple,dict,set
# l=[1,2,3,4,5]
# for i in l:
# 	print(i)

# #sum of list
# l=[1,2,3,4,5]
# sum=0
# for i in l:
# 	sum+=i
# print("Addition of all numbersof the list: ",sum)

# #sum of numbers one by one and also display the result one by one
# l=[1,2,3,4,5]
# sum=0
# for i in l:
# 	print(sum)
# 	sum+=i

##or
# l=[1,2,4]
# print(sum(l))

# #range--always upto (n-1)
# #range(5)--0 1 2 3 4
# #range(10,100)--10 11 12 13......99
# #range(10,100,5)--10 15 20 25 30 35....90 95 
# for value in range(10,100,8):
# 	print(value)

# sum=0
# for value in range(11):  #inplace of we also write(1,11)
# 	sum+=value
# print(sum)

# #######Session3
# #break,continue
# l=[1,2,3,4,5,4]
# key=4
# for i in l:
# 	if i==key:
# 		print("Element found")
# 		break
# 	else:
# 	    continue	
# else:
#     print("Element not found")	    

# #enumerate
# l=[1,2,3,4,5]
# for index,value in enumerate(l):
# 	print(index,value)

# #if we write any thing after the continue it can't be execute because continue transfer the code  
# l=[1,2,3,4,5,4]
# key=4
# for index,value in enumerate(l):
# 	if value==key:
# 		print("Element found at index: ",index)
# 		break       #continue in place of break it return all index where the key is 
# 	else:
# 	    continue
# 	    print("continue")	
# else:
#     print("Element not found")	    

# #but if we write pass it will be executed
# l=[1,2,3,4,5]
# key=4
# for index,value in enumerate(l):
# 	if value==key:
# 		print("Element found at index: ",index)
# 		break
# 	else:
# 	    pass
# 	    print("Continue to find the key")
# else:
#     print("Element not found")

########Session4
## while loop
# while [condition]:
# 	statement
# else:	

# #1-20 numbers
# count=1
# sum=0
# while count<=20:
# 	sum+=count
# 	count+=1
# print(sum)

# # #Questions--
##(1)WAP to find those numbers which are divisible by 7 and 5, between 1500 and 2700(both included).	
# print("First and Last number for range:")
# f=int(input("Enter Starting number: "))
# l=int(input("Enter last number: "))
# l1=[]
# for i in range(f,l+1):
# 	if i%7==0 and i%5==0:
#          print(i,end=",")
# print()

# ##print in a list
# print("First and Last number for range where numbers are divisible by 5 and 7 :")
# f=int(input("Enter Starting number: "))
# l=int(input("Enter last number: "))
# l1=[]
# for i in range(f,l+1):
# 	if i%7==0 and i%5==0:
#          #print(i,end=",")
#          l1.append(i)
# print(l1)
# print()

# ##without comma in the end of the output
# print("First and Last number for range:")
# f=int(input("Enter Starting number: "))
# l=int(input("Enter last number: "))
# l1=[]
# for i in range(f,l+1):
# 	if i%7==0 and i%5==0:
#          l1.append(str(i))
# output=",".join(l1)
# print(output)
# print()

##(2)WAP to count the number of even and odd numbers from a series of numbers.
# t=input("Enter numbers: ").split(",")
# t1=(tuple(map(int,t)))
# print("numbers in tuple:",t1)
# count_even=0
# count_odd=0
# for i in t1:
#     if i%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
# print("even numbers: ",count_even) 
# print("Odd numbers: ",count_odd)

## 3)WAP which iterates the integers from 1 to 50.
##for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
##for numbers which are multiples of both three and five print "FIzzBuzz".
# for i in range(1,50+1):
#     if i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0 and i%5==0:
#         print("FizzBuzz")
#     else:
#         print(i)

##4)WAP to calculate the sum and average of n integers numbers.
# n=input("Enter numbers:").split(",")
# print(n)
# sum=0
# avg=0
# for i in n:
#     sum+=int(i)
# avg=sum/len(n)
# print(sum)
# print(avg)

##5)Factorial of any n is represented by n! and is equal to 1*2*3*..*(n-1)*n.
##calculate factorial of a number.
# n=int(input("Enter number: "))
# s=1
# l=[]
# for i in range(1,n+1): 
#     if n==1 and n==0:
#         print(n,"!=1")
#     else:
#         s*=i
#         l.append(str(i)) 
# output="*".join(l)               
# print(n,"!=",output,"=",s)
