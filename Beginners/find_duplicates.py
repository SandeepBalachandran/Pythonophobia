# check for duplicates

some_list = ['a','b','c','b','m','n','n']

# sets = set(some_list)
# print(sets)

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
# print(duplicates)

duplicates2 = list(set([x for x in some_list if some_list.count(x)>1]))
print(duplicates2)

# def test(a):
#     '''
#     Info : this is placeholder
#     '''
#     print(a)

# help(test)
# print(test.__doc__)

# def super_func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     return sum(args)

# print(super_func(1,2,3,4,5,num1=5,num2=10))

#Rule params,*args,default params,**kwargs

