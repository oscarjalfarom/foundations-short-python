tuplen = (1, 2, 3)
tuple_of_tuples = ()
lengt_tuple_of_tuples = 2**(len(tuplen))
temp = ()

#for index in range(lengt_tuple_of_tuples):
if len(temp) == 0:
    temp = (temp, )
for element in tuplen:
    temp = tuplen + ("",) + temp
        #tuple_of_tuples = tuple_of_tuples + (temp,)

#print(tuple_of_tuples)
print(temp)
