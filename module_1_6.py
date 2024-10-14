my_dict = {'name': 'Светлана', 'age': 40}
print(my_dict)
print(my_dict['name'])
print(my_dict.get('login'))

my_dict['login'] = 'user 1'
my_dict['password'] = '12345'

my_dict.pop('login')
#print(my_dict['password'])
print(my_dict)

my_set = {1,2,'Светлана', 2, 2}
print(my_set)
my_set.add(10)
my_set.add(11)
print(my_set)
my_set.remove(11)
print(my_set)
