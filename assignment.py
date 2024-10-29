my_list = [i for i in range(10,50,10)]
my_list.insert(1,15)
my_list += [i for i in range(50,80,10)]
my_list.pop()
my_list.sort()
print(my_list.index(30))