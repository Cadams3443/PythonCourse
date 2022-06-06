x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][1] = 15

students[1]['last_name'] = "Bryant"

sports_directory["soccer"][0] = "Andres"

z[0]['y'] = 30


student = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

key1 = "first_name"
key2 = "last_name"

def iterateDictionary0(some_list):
    for x in range (0, len(some_list)):
        print(key1, "=", some_list[x][key1], key2, "=", some_list[x][key2])

iterateDictionary0(student)

def iterateDictionary(some_list):
    for x in range (0, len(some_list)):
        print(some_list[x][key1],some_list[x][key2])

iterateDictionary(student)        

def iterateDictionary1(some_list):
    for x in range (0, len(some_list)):
        print(some_list[x][key1])

iterateDictionary1(student)

def iterateDictionary2(some_list):
    for x in range (0, len(some_list)):
        print(some_list[x][key2])

iterateDictionary2(student)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

key3 ='locations'
key4 = 'instructors'


def printInfo(some_dict):
    print(len(some_dict[key3]), key3)
    for x in range (0, len(some_dict[key3])):
        print(some_dict[key3][x])
    print(len(some_dict[key4]), key4)
    for y in range (0, len(some_dict[key4]) ):
        print(some_dict[key4][y])



printInfo(dojo)

