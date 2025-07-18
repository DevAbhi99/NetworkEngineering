#dictionaries are like objects in other programming languages like java or javascript

employee={
    "name":"Karan",
    "age":21,
    "skills":{
        "Programming languages":["python", "javascript", "java"],
        "tech stack":["networking", "full stack engineer"]
    }
}

print(employee["name"])

print(employee["skills"]["Programming languages"])

#update or add another :-update({key:value}}

employee.update({"salary":100000000})

print(employee)