list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]

print(list_to_sort)

list_to_sort.sort(key=lambda x: (x[1],x[2]))

print(list_to_sort)

password = 'python'

number_of_tries = 10
while number_of_tries > 0:
    val = input('podaj haslo')
    if val==password:
        print('gratulacje')
        break
    else:
        continue
    number_of_tries -= 1
if number_of_tries==0:
    print('przegrales')

from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]

import time
start_time = time.time()
for num in long_list:
    if num == -1:
        print(num)
print(time.time()-start_time)

start_time2 = time.time()
counter = len(long_list)-1
while counter>0:
    if long_list[counter]==-1:
        print(long_list[counter])
    counter -=counter
print(time.time()-start_time2)

start_time3 = time.time()
if -1 in long_list:
    print('found')
print(time.time() - start_time3)

start_time4 = time.time()
if -1 not in long_list:
    pass
else:
    print('found')
print(time.time() - start_time4)

names = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']

letters_array = [element[0] for element in names]

print(letters_array)


