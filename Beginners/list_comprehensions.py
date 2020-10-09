#list,set, dictionary

#list comprehensions

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num **2 for num in range(0,100)]
my_list4 = [num **2 for num in range(0,100) if num%2 == 0] 
print(my_list4)
#set comprehenstions

my_list5 = {char for char in 'hello'}
my_list6 = {num for num in range(0,100)}
my_list7 = {num **2 for num in range(0,100)}
my_list8 = {num **2 for num in range(0,100) if num%2 == 0} 
print(my_list8)

# dictionary comprehensions

simple_dict = {
    'a' :1,
    'b' : 2
}
my_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict)

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)