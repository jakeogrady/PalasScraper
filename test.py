
list = []


for i in range(2):
    dict = {}
    name = input("Enter a name here please: ")
    age = input("Enter age here: ")
    dict['name'] = name
    dict['age'] = age
    list.append(dict)
    
for i in range(0,len(list)):
    print(list[i])