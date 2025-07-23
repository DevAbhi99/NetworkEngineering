#Hashmap

hm={}

#Creating key value pair

hm[1]="one"

hm[2]="two"

hm[3]="three"

print(hm)

#updating value

hm[3]="four"

print(hm)

print(len(hm))

#deleting data on the basis of key

del hm[3]

print(hm)

#Check

if 2 in hm:
    print("yes")

#Looping through dictionary

for key, value in hm.items():
    if key%2==0:
        print(value)



 #Storing duplicate characters in string

str="sddaavvvcc" 

n1=len(str)

hash={}



for i in range(0,n1):
    if str[i] in hash:
        hash[str[i]]+=1
    else:
        hash[str[i]]=1

print(hash)        