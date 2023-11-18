mi_tupla = 1, 2, 3
sub_mi_tupla = ((), (1, ), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3))
print(sub_mi_tupla)
newTuple = ()
for index in range(len(sub_mi_tupla)):
  for subIndex in range(len(sub_mi_tupla[index])):  
    newTuple = (sub_mi_tupla[index][subIndex], ) + newTuple
print(newTuple)
