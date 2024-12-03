my_dict = {'Gray': 1990, 'Groover': 1989, 'Alesha': 1994, 'Vladislav':1993 }
print (my_dict)
print (my_dict['Gray'])
my_dict["Leroy"]=1996
print (my_dict)
my_dict.update({'Lora': 1986,
                'Axel': 1999})
del my_dict['Gray']
print (my_dict.get('Gray'))
print (my_dict)

my_set ={1, 1, "Leroy", "Leroy", 'leroy', 2.2, 2.2, (1, 3, 6), (1, 3, 6)}
print (my_set)
my_set.add(4) #воспользовался командой .add, как в видеоуроке
my_set.add(5)
my_set.update ([13,14]) #воспользовался командой update, для того чтобы за 1 команду добавить несколько значений, для практики.
my_set.discard(2.2)
print (my_set)

