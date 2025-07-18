#Loops:- For loop and while loop

#while loop

#from 1 to 10 print only even numbers

i=1

while(i<=10):
    if i%2==0:
        print(i)
    i+=1

#for loop

#from 1 to 10 print only even numbers

for j in range(1,10):
    if j%2==0:
        print(j)


#break statement breaks the loop and continue statement continue the loop

#To find if a number is prime or not

num=2

flag=0


for i in range(2,num):
    if num%i==0:
        flag=1
        break




if flag==1:
    print('Not Prime')
else:
    print('prime')
    
