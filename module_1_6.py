my_dict = {'name': 'Светлана', 'age': 40}
print(my_dict)
print(my_dict['name'])
try:
    print(my_dict['login'])
except:
    print('Error key dict')

my_dict['login'] = 'user 1'
my_dict['password'] = '12345'

del my_dict['password']
#print(my_dict['password'])
print(my_dict)

my_set = {1,2,'Светлана', 2, 2}
print(my_set)
my_set.add(10)
my_set.add(11)
print(my_set)
my_set.remove(11)
print(my_set)
