#tuples are lists in 

tuple1=(1,2,3,4,4)

print(tuple1)


# functions

# 1) count(element):- find the number of occurences in tuple

print(tuple1.count(4))

#2) index(element):- returns the position of the element in the tuple

print(tuple1.index(4))


##Basic programs

lists=[1,0,2,0,3,0,4,0,5]

#in the above list remove zeroes without changing order of the list

t=tuple(lists)

count=t.count(0)

for i in range(1,count+1):
    lists.remove(0)

print(lists)
