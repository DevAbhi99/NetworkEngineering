#lists are datastructures just like arrays in other programming languages

arr=[1,2,3,4,5,6]

print(arr)

#functions

#1) len() :- length of array

print(len(arr))

#2) accessing array just like string

print(arr[0])

#3) reverse() :- reverse the array

arr.reverse()

print(arr)

#4) sort() :- sort the array

arr.sort()

print(arr)

#5) slicing in array just like string

print(arr[1:5])

#6) + joins two lists

arr1=[1,2]

arr2=[3,4]

res=arr1+arr2

print(res)

#7) list1=list2 copies one array to another

arr3=res

print(arr3)


#8) Modifying elements in array:- just access the element and assign a value

arr[1]=9

#9) append(element) :- adding element in the array

arr.append(10)

#10) deleting element in the array

#) pop(index) :- removes element at the mentioned position

arr.pop(0) #removes 1

print(arr)
#) remove(element) :- removes the element mentioned

arr4=[1,1,1,2,3,4]

arr4.remove(1)

print(arr4)





#Basic programs

lists=[1,0,2,0,3,0,4,0,5]

#in the above list remove zeroes without changing order of the list

count=0

for i in range(0, len(lists)):
    if lists[i]==0:
        count+=1


for i in range(1, count+1):
    lists.remove(0)

print(lists)


#Two Dimensional list

twod=[[1,2,3],[4,5,6]]

print(twod)

row=len(twod)

col=len(twod[0])

print(row)

print(col)