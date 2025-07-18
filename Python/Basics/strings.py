#string functions

s='hey man'

#1) capitalize():- converts the first character of a string to uppercase

print(s.capitalize())


#2) upper():- converts the entire string to upper case

print(s.upper())

#3) lower():- converts the entire string to lower case

s1=s.upper()

print(s1)

print(s1.lower())

#4) find() :- find the substring in a string and return its position

print(s.find('y'))

#5) lstrip():- removes spaces from left sides

x=' hey man '

print(x.lstrip())

#6) rstrip():- removes spaces from the right side

print(x.rstrip())

#7) strip():- removes spaces from both sides

print(x.strip())

#8) slicing in a string

# fetch hey from string

print(s[0:3])

#9) split() splits string in list

arr=s.split()

print(arr)

#10) list() converts characters to list

chars=list(s)

print(chars)

#11) replace(old string, newstring) :- replace old string with new string

string='yyaayyyb'

string2=string.replace('yy','ss')

print(string2)

#12) len():- find length of the string

print(len(s))

#13) startsWith():- to find if the string starts with the character

print(s.startswith('h')) 

#14) endsWith():- to find if the string ends with the character

#15) Accessing a character in a string string[index]

print(s[1])







#code to loop through a string and return only vowel in the string

for i in range(0, len(s)):
    if s[i]=='a' or s[i]=='e'or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E'or s[i]=='I' or s[i]=='O' or s[i]=='U':
        print(s[i])


# loop through and find if a substring exists in a string

target='hey'

flag=0

for i in range(0, len(s)):
    if s.find(s[i])==-1:            
        flag=1


if flag==0:
    print('Found at position', s.find(target))
else:
    print('Not found')


    #16) zfill(number) :- fills number of zeroes before the string



print('5'.zfill(5))
